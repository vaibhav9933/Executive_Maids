from flask import Flask, render_template, request, redirect, url_for, session,flash
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Vaibhav@123'
app.config['MYSQL_DB'] = 'maid4'

mysql = MySQL(app)

# Create tables if they don't exist
with app.app_context():
    cursor = mysql.connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS maids (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            phone_no VARCHAR(15),
            email VARCHAR(100) UNIQUE,
            aadhar VARCHAR(12),
            address TEXT,
            food_preference ENUM('veg', 'nonveg', 'both'),
            skills TEXT,
            gender ENUM('male', 'female', 'other'),
            location VARCHAR(100),
            profile_pic VARCHAR(255)
        );
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            phone_no VARCHAR(15),
            email VARCHAR(100) UNIQUE
        );
    ''')
    cursor.execute('''
CREATE TABLE if not exists contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(255),
    message TEXT);
''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            id INT AUTO_INCREMENT PRIMARY KEY,
            customer_id INT,
            maid_id INT,
            food_preference ENUM('veg', 'nonveg', 'both'),
            service_type ENUM('cleaning', 'washing', 'child_care', 'elder_care'),
            booking_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (customer_id) REFERENCES customers(id),
            FOREIGN KEY (maid_id) REFERENCES maids(id)
        );
    ''')
    mysql.connection.commit()
    cursor.close()

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/index.html')
def home1():
    return render_template('index.html')
@app.route('/contact.html')
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        # Create a cursor object to interact with the database
        cur = mysql.connection.cursor()

        # Insert data into MySQL database
        cur.execute("INSERT INTO contacts(name, email, phone, message) VALUES(%s, %s, %s, %s)", (name, email, phone, message))
        mysql.connection.commit()

        # Close the cursor
        cur.close()

        # Show a flash message
        flash('Your message has been sent! You will receive a resolution of your query soon.', 'success')

        # Redirect to the same page
        return redirect(url_for('contact'))

    return render_template('contact.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_type = request.form['user_type']
        email = request.form['email']
        # Add login logic here (for simplicity, not implemented)
        return redirect(url_for('dashboard', user_type=user_type))
    return render_template('login.html')

@app.route('/dashboard/<user_type>')
def dashboard(user_type):
    if user_type == 'maid':
        return render_template('maids_dashboard.html')
    else:
        return render_template('customers_dashboard.html')
    
@app.route('/customers_dashboard.html')
def customers_dashboard():
    render_template('customers_dashboard.html')

@app.route('/register.html')
def register():
    return render_template('register.html')


@app.route('/register_maid', methods=['GET', 'POST'])
def register_maid():
    if request.method == 'POST':
        name = request.form['name']
        phone_no = request.form['phone_no']
        email = request.form['email']
        aadhar = request.form['aadhar']
        address = request.form['address']
        food_preference = request.form['food_preference']
        skills = request.form['skills']
        gender = request.form['gender']
        location = request.form['location']
        profile_pic = request.form['profile_pic']

        cursor = mysql.connection.cursor()
        cursor.execute('''
            INSERT INTO maids (name, phone_no, email, aadhar, address, food_preference, skills, gender, location, profile_pic)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''', (name, phone_no, email, aadhar, address, food_preference, skills, gender, location, profile_pic))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('login'))
    return render_template('maid.html')

@app.route('/register_customer', methods=['GET', 'POST'])
def register_customer():
    if request.method == 'POST':
        name = request.form['name']
        phone_no = request.form['phone_no']
        email = request.form['email']

        cursor = mysql.connection.cursor()
        cursor.execute('''
            INSERT INTO customers (name, phone_no, email) VALUES (%s, %s, %s)
        ''', (name, phone_no, email))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('login'))
    return render_template('customer.html')



@app.route('/search_maids', methods=['GET'])
def search_maids():
    query = request.args.get('query')
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM maids WHERE name LIKE %s', ('%' + query + '%',))
    matching_maids = cursor.fetchall()
    cursor.close()
    return render_template('search_results.html', maids=matching_maids)

@app.route('/booking_history')
def booking_history():
    customer_id = session.get('customer_id')  # Assuming customer_id is stored in session
    cursor = mysql.connection.cursor()
    cursor.execute('''
        SELECT bookings.*, maids.name AS maid_name FROM bookings
        JOIN maids ON bookings.maid_id = maids.id
        WHERE bookings.customer_id = %s
    ''', (customer_id,))
    booking_data = cursor.fetchall()
    cursor.close()
    return render_template('booking_history.html', bookings=booking_data)

@app.route('/admin_dashboard')
def admin_dashboard():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM maids')
    all_maids = cursor.fetchall()
    cursor.execute('SELECT * FROM customers')
    all_customers = cursor.fetchall()
    cursor.close()
    return render_template('admin_dashboard.html', maids=all_maids, customers=all_customers)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

@app.route('/about_us.html')
def aboutus():
    return render_template('about_us.html')
maids = [
    {'maid_id': 1, 'maid_name': 'Priyanka Sharma', 'maid_skills': 'Cleaning, Cooking, Child Care'},
    {'maid_id': 2, 'maid_name': 'Anita Desai', 'maid_skills': 'Cleaning, Elder Care'},
    # Add other maids as needed
]

# Route to display the booking form
@app.route('/book_maid/<int:maid_id>', methods=['GET'])
def book_maid(maid_id):
    maid = next((maid for maid in maids if maid['maid_id'] == maid_id), None)
    if maid:
        return render_template('booking_form.html', maid_id=maid['maid_id'], maid_name=maid['maid_name'])
    return "Maid not found", 404

# Route to handle the form submission
@app.route('/submit-booking', methods=['POST'])
def submit_booking():
    customer_name = request.form['customer_name']
    address = request.form['address']
    phone = request.form['phone']
    maid_id = request.form['maid_id']
    maid_name = request.form['maid_name']

    # Save booking to the database (simulated here with a flash message)
    flash(f"Booking confirmed for {customer_name}. Maid {maid_name} will assist you soon!")

    return redirect(url_for('confirm_booking', customer_name=customer_name, maid_name=maid_name))

# Route to show booking confirmation
@app.route('/confirm-booking')
def confirm_booking():
    customer_name = request.args.get('customer_name')
    maid_name = request.args.get('maid_name')
    return render_template('confirm_booking.html', customer_name=customer_name, maid_name=maid_name)

@app.route('/reviews.html')
def review():
    return render_template('reviews.html')


if __name__ == '__main__':
    app.run(debug=True)




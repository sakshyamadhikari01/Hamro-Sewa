from flask import Flask, render_template,request,session,redirect
import random
from datetime import datetime


app = Flask(__name__)
app.secret_key = 'hamrosewa_secret_key' \


#language dictionary
LANG = {
    'en': {
     'home': 'Home',
        'contacts': 'Contacts',
        'team': 'Meet Our Team',
        'login': 'Login',
        'register': 'Register',
        'welcome': 'Welcome to',
        'enter_website': 'Enter Website',
        'customer_dashboard': 'Customer Dashboard',
        'professional_dashboard': 'Professional Dashboard',
        'book_now': 'Book Now',
        'send': 'Send',
        'confirm_booking': 'Confirm Booking',
        'quality_home_services': 'Quality home services, on demand',
        'service_available_in': 'Service available in:',
        'about': 'About Hamro Sewa',
        'how_it_works': 'How It Works',
        'featured_professionals': 'Featured Professionals',
        'why_hamro_sewa': 'Why Hamro Sewa?',
        'experts_only': 'Experts Only',
        'transparent_pricing': 'Transparent Pricing',
        'fully_equipped': 'Fully Equipped',
        'quality_assured': 'Quality Assured',
        'what_customers_say': 'What Our Customers Say',
        'register_title': 'Register',
        'login_title': 'Login',
        'contacts_title': 'Contact Us',
        'nepali': 'नेपाली',
        'english': 'English'
    }
}
@app.ruote('/home')
def home():
    lang_code = session.get('lang', 'en')
    lang = LANG.get(lang_code, LANG['en'])
    return render_template('index.html', lang=lang)

#simulated buys slots and   chat history database
buys_slots_db = {}
chat_history_db = {}

@app.route('/team')
def team():
    lang_code = session.get ('lang', 'en')
    lang = LANG.get(lang_code, LANG['en'])
    return render_template('team.html', lang=lang)

#booking route
@app.route('/book/<job>/<name>', methods=['GET', 'POST'])
def book(job, name):
    #find professional 
    prof = next((p for p in professionals.get(job.lower(), []) if p['name'] == name), None)
    if not prof:
        return "Professional not found", 404
    
    #Simulate available slots
    available_slots = [f"{h}:00" for h in range(9,18)]
    date=request.form.get('date') or datetime.now().strftime('%Y-%m-%d')
    buys_slots_db.get((name,date),[])
    chat_history_db.get((name,job),[])
    if request.method == 'POST' and 'time' in request.form:
        team=request.form['time']
        if time in busy_slots:
            message = f'{prof["name"]} is busy at {time}. Please choose another time.'
           else:
           buys_slots.append(time)
           buys__slots_db[(name,date)] = buys_slots
           messgae = F"BOooking confirmed with {prof{'name'} at {time} on {date}."

 lang_code =sesssion.get('lang','en')
    lang = get(LANG.get(lang_code, LANG['en'])  
               return render_template('book.html', prof=prof, available_slots=available_slots, date=date, busy_slots=busy_slots, message=message, lang=lang)

               #chat route
               @app.route('/chat/<job>/<name>', methods=['GET', 'POST'])
def chat(job, name):
    prof = next((p for p in professionals.get(job.lower(), []) if p['name'] == name), None)
    if not prof:
    return "Professional not found", 404
    chat_history_db.get((name,job),[])
if msg text:
chat_history.append({'sender': 'user', 'text': msg_text })
chat_history.append({'sender':prof['name'],'text':"Thank you for your message. I will get back to you shortly."})

#Simulate available slots
available_slots =[f"{h}:00" for h in range(9,18)]
date = datetime.now().strftime('%Y-%m-%d')
buys_slots = buys_slots_db.get((name,date),[])
lang_code = session.get('lang', 'en')
lang = LANG.get(lang_code, LANG['en'])
 available_slots=available_slots, date=date, busy_slots=busy_slots, chat_history=chat_history, lang=lang)

import time

#Sample data for profesionals
professionals = {
    'electrician': [
        {'name': 'Ram Shrestha', 'contact': '9800000001', 'rating': 4.5, 'experience': '5 years', 'image': 'https://randomuser.me/api/portraits/men/32.jpg'},
        {'name': 'Sita Gurung', 'contact': '9800000002', 'rating': 4.2, 'experience': '3 years', 'image': 'https://randomuser.me/api/portraits/women/44.jpg'},
        {'name': 'Hari Thapa', 'contact': '9800000003', 'rating': 4.8, 'experience': '7 years', 'image': 'https://randomuser.me/api/portraits/men/65.jpg'}
    ],
    'plumber': [
        {'name': 'Gopal Lama', 'contact': '9800000011', 'rating': 4.1, 'experience': '2 years', 'image': 'https://randomuser.me/api/portraits/men/12.jpg'},
        {'name': 'Manju Karki', 'contact': '9800000012', 'rating': 4.6, 'experience': '6 years', 'image': 'https://randomuser.me/api/portraits/women/36.jpg'},
        {'name': 'Bikash Rai', 'contact': '9800000013', 'rating': 4.3, 'experience': '4 years', 'image': 'https://randomuser.me/api/portraits/men/23.jpg'}
    ],
    'carpenter': [
        {'name': 'Krishna Tamang', 'contact': '9800000021', 'rating': 4.7, 'experience': '8 years', 'image': 'https://randomuser.me/api/portraits/men/41.jpg'},
        {'name': 'Puja Magar', 'contact': '9800000022', 'rating': 4.4, 'experience': '5 years', 'image': 'https://randomuser.me/api/portraits/women/22.jpg'},
        {'name': 'Ramesh KC', 'contact': '9800000023', 'rating': 4.0, 'experience': '3 years', 'image': 'https://randomuser.me/api/portraits/men/77.jpg'}
    ]
}


#reditect root URL to the homepage (e.g., service or login or index.html)
from flask import redirect,url_for,session 

@app.route('/')
def index():
    lang_code =session . get ('lang','en' )
lang = LANG.get(lang_code, LANG['en'])
#Render the main homepage instead of welcome page
return rebnder_template('index.html', lang=lang)


                        




    
 

                                        


                            




           
           
'')

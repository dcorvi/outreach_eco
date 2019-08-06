from app import app
from flask import render_template, url_for, redirect, flash
from app.forms import ContactForm, VIPOfferForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Index')


@app.route('/products')
def products():
    return render_template('products.html', title='Products')

@app.route('/vip_offers')
def vip_offers():
    form = VIPOfferForm()

    if form.validate_on_submit():
        try:
            contact = Contact(
                name = form.name.data,
                email = form.email.data
            )

            # db.session.add(contact)
            # db.session.commit()

            flash(f'Thanks for your submission, we will contact you shortly. A copy has been sent to {form.email.data}')
            return redirect(url_for('index'))
        except:
            flash('Sorry your submission did not go through. Try again.')
            return redirect(url_for('vip_offers'))

    return render_template('vipoffers.html', form=form, title='VIP Special Offers')

@app.route('/blog')
def blog():
    return render_template('blog.html', title='Blog')

@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        try:
            contact = Contact(
                name = form.name.data,
                email = form.email.data,
                message = form.message.data
            )

            # db.session.add(contact)
            # db.session.commit()

            flash(f'Thanks for your submission, we will contact you shortly. A copy has been sent to {form.email.data}')
            return redirect(url_for('index'))
        except:
            flash('Sorry your submission did not go through. Try again.')
            return redirect(url_for('contact'))

    return render_template('contact.html', form=form, title='Contact')

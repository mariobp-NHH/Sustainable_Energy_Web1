import os
import secrets
import json
from datetime import timedelta, datetime
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort, jsonify, Blueprint
from webse import app, db, bcrypt
from webse.chats.forms import ChatFormUpdate
from webse.models import Userpage, Moduls, Announcement, Chat, Emissions
from flask_login import login_user, current_user, logout_user, login_required
from webse.users.utils import read_image

chats = Blueprint('chats', __name__)

##################################
####   Block 3. Query chat    ####
##################################

@chats.route('/chat_web', methods=['GET', 'POST'])
@login_required
def chat_web():
    return render_template('chat/chat_web.html', title='Chat Web')

@chats.route('/chat_web/chat_home')
@login_required
def chat_web_chat_home():
    page = request.args.get('page', 1, type=int)
    chats = Chat.query.filter(Chat.chat_module=='Home Chat').order_by(Chat.date_posted.desc()).paginate(page=page, per_page=4)
    return render_template('chat/chat_home.html', chats=chats, title=' Chat Home', legend='Home Chat',func=read_image)

@chats.route('/chat_web/chat_informal')
@login_required
def chat_web_chat_informal():
    page = request.args.get('page', 1, type=int)
    chats = Chat.query.filter(Chat.chat_module=='Informal Chat').order_by(Chat.date_posted.desc()).paginate(page=page, per_page=4)
    return render_template('chat/chat_informal.html', chats=chats, title='Chat informal', legend='Informal Chat', func=read_image)

@chats.route('/chat_web/chat_app_g1')
@login_required
def chat_web_chat_app_g1():
    page = request.args.get('page', 1, type=int)
    chats = Chat.query.filter(Chat.chat_module=='App Module Chat').\
        filter(Chat.chat_group=='Group 1').order_by(Chat.date_posted.desc()).paginate(page=page, per_page=4)
    return render_template('chat/chat_app_g1.html', chats=chats, title=' Chat App G1', legend='App Module Chat, Group 1',
                           paragraph='Moni (Monica), KieranClark, Solveig, Kleppe (Peder), Rebecca, ethan.mcchristian, Ivanessa, Katharina, Hala', func=read_image)

@chats.route('/chat_web/chat_app_g2')
@login_required
def chat_web_chat_app_g2():
    page = request.args.get('page', 1, type=int)
    chats = Chat.query.filter(Chat.chat_module=='App Module Chat').\
        filter(Chat.chat_group=='Group 2').order_by(Chat.date_posted.desc()).paginate(page=page, per_page=4)
    return render_template('chat/chat_app_g2.html', chats=chats, title=' Chat App G2', legend='App Module Chat, Group 2',
                           paragraph='Veronika, csalvati (Cristina), Krossland (Kristian), elizaveta.goncharova, Sabrina, Steffen, Vanessa, Axel', func=read_image)

@chats.route('/chat_web/chat_app_g3')
@login_required
def chat_web_chat_app_g3():
    page = request.args.get('page', 1, type=int)
    chats = Chat.query.filter(Chat.chat_module=='App Module Chat').\
        filter(Chat.chat_group=='Group 3').order_by(Chat.date_posted.desc()).paginate(page=page, per_page=4)
    return render_template('chat/chat_app_g3.html', chats=chats, title=' Chat App G3', legend='App Module Chat, Group 3',
                           paragraph='Marita, Paula, paolo rossi, runar_johnston, Louise, mitcht (Mitchell), Klara, Yasmina', func=read_image)

@chats.route('/chat_web/chat_app_g4')
@login_required
def chat_web_chat_app_g4():
    page = request.args.get('page', 1, type=int)
    chats = Chat.query.filter(Chat.chat_module=='App Module Chat').\
        filter(Chat.chat_group=='Group 4').order_by(Chat.date_posted.desc()).paginate(page=page, per_page=4)
    return render_template('chat/chat_app_g4.html', chats=chats, title=' Chat App G4', legend='App Module Chat, Group 4',
                           paragraph='Seb (Sebastian), Leonora Skorpen, conte, fabian, Marthine, FilipF, Tiphaine, Igor, Marius', func=read_image)

@chats.route('/chat_web/chat_app_g5')
@login_required
def chat_web_chat_app_g5():
    page = request.args.get('page', 1, type=int)
    chats = Chat.query.filter(Chat.chat_module=='App Module Chat').\
        filter(Chat.chat_group=='Group 5').order_by(Chat.date_posted.desc()).paginate(page=page, per_page=4)
    return render_template('chat/chat_app_g5.html', chats=chats, title=' Chat App G5', legend='App Module Chat, Group 5',
                           paragraph='Ruth, ashish.kumar, marfjo (Maria), Marenoj (Maren), petnyg (Petter), Addison Liandong Wu, Mokhinur, Jon Heine, Kristoffer Jansen', func=read_image)

@chats.route('/chat_web/chat_se_g1')
@login_required
def chat_web_chat_se_g1():
    page = request.args.get('page', 1, type=int)
    chats = Chat.query.filter(Chat.chat_module=='Sustainable Energy Module Chat').\
        filter(Chat.chat_group=='Group 1').order_by(Chat.date_posted.desc()).paginate(page=page, per_page=4)
    return render_template('chat/chat_se_g1.html', chats=chats, title=' Chat SE G1', legend='Sustainable Energy Module Chat, Group 1',func=read_image,
                           paragraph1='Fabion Abazaj, Liandong Wu, Kristian Sj??en Rossland, Maren Johansen ??yan, Marthine Hjart??ker Ingebrigtsen, Petter Sveen Nygaard',
                           paragraph2='Nuclear energy and Renewable Energy Sources')


@chats.route('/chat_web/chat_se_g2')
@login_required
def chat_web_chat_se_g2():
    page = request.args.get('page', 1, type=int)
    chats = Chat.query.filter(Chat.chat_module=='Sustainable Energy Module Chat').\
        filter(Chat.chat_group=='Group 2').order_by(Chat.date_posted.desc()).paginate(page=page, per_page=4)
    return render_template('chat/chat_se_g2.html', chats=chats, title=' Chat SE G2', legend='Sustainable Energy Module Chat, Group 2',func=read_image,
                           paragraph1='Runar Hauk??s Johnston, Elizaveta Goncharova, Sebastian Bergseth, Veronika Priakhina, Louise Nicolini, Agathe Brattaule',
                           paragraph2='Political gender balance effect on renewables in the energy mix')

@chats.route('/chat_web/chat_se_g3')
@login_required
def chat_web_chat_se_g3():
    page = request.args.get('page', 1, type=int)
    chats = Chat.query.filter(Chat.chat_module=='Sustainable Energy Module Chat').\
        filter(Chat.chat_group=='Group 3').order_by(Chat.date_posted.desc()).paginate(page=page, per_page=4)
    return render_template('chat/chat_se_g3.html', chats=chats, title=' Chat SE G3', legend='Sustainable Energy Module Chat, Group 3',func=read_image,
                           paragraph1='Paolo Rossi, Sabrina Hartenfels, Vanessa Wickel, Paula Jimenez Gomez, Klara Wolschlager',
                           paragraph2='Tidal energy')

@chats.route('/chat_web/chat_se_g4')
@login_required
def chat_web_chat_se_g4():
    page = request.args.get('page', 1, type=int)
    chats = Chat.query.filter(Chat.chat_module=='Sustainable Energy Module Chat').\
        filter(Chat.chat_group=='Group 4').order_by(Chat.date_posted.desc()).paginate(page=page, per_page=4)
    return render_template('chat/chat_se_g4.html', chats=chats, title=' Chat SE G4', legend='Sustainable Energy Module Chat, Group 4',func=read_image,
                           paragraph1='Hala Al Jamal, Cristina Salvati, Ivanessa Staykova, Keiran Clark, Monica Schwartzel, Peder Sebastian Kleppe',
                           paragraph2='Energy storage and its interplay with the mining and sustainable energy industries')

@chats.route('/chat_web/chat_se_g5')
@login_required
def chat_web_chat_se_g5():
    page = request.args.get('page', 1, type=int)
    chats = Chat.query.filter(Chat.chat_module=='Sustainable Energy Module Chat').\
        filter(Chat.chat_group=='Group 5').order_by(Chat.date_posted.desc()).paginate(page=page, per_page=4)
    return render_template('chat/chat_se_g5.html', chats=chats, title=' Chat SE G5', legend='Sustainable Energy Module Chat, Group 5',func=read_image,
                           paragraph1='Steffen Nathan, Maria Sels??s, Ashish Kumar, Leopold Reinisch, Jon Heine, Filip Fandel',
                           paragraph2='Agrivoltaics -The use of croplands for both agriculture and solar energy at the same time')

@chats.route('/chat_web/chat_se_g6')
@login_required
def chat_web_chat_se_g6():
    page = request.args.get('page', 1, type=int)
    chats = Chat.query.filter(Chat.chat_module=='Sustainable Energy Module Chat').\
        filter(Chat.chat_group=='Group 5').order_by(Chat.date_posted.desc()).paginate(page=page, per_page=4)
    return render_template('chat/chat_se_g6.html', chats=chats, title=' Chat SE G6', legend='Sustainable Energy Module Chat, Group 6',func=read_image,
                           paragraph1='Axel ??stby, Leonora Leine Skorpen, Marius Slette, Kristoffer Jansen',
                           paragraph2='...')

###################################################
####   Block 4. Create, update, delete chat    ####
###################################################

@chats.route("/chat_new", methods=['GET', 'POST'])
@login_required
def new_chat():
    return render_template('chat/new_chat.html', title='Chat Web')

@chats.route("/chat_new/create/home", methods=['GET', 'POST'])
@login_required
def new_chat_create_home():
    form = ChatFormUpdate()
    if form.validate_on_submit():
        chat = Chat(title=form.title.data, content=form.content.data, author=current_user, chat_module='Home Chat',
                     chat_group='All')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('chats.chat_web'))
    return render_template('chat/create_chat_home.html', title='Create Chat', form=form,legend='Home Chat')

@chats.route("/chat_new/create/informal", methods=['GET', 'POST'])
@login_required
def new_chat_create_informal():
    form = ChatFormUpdate()
    if form.validate_on_submit():
        chat = Chat(title=form.title.data, content=form.content.data, author=current_user, chat_module='Informal Chat',
                     chat_group='All')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('chats.chat_web'))
    return render_template('chat/create_chat_informal.html', title='Create Chat', form=form,legend='Informal Chat')

@chats.route("/chat_new/create/app_g1", methods=['GET', 'POST'])
@login_required
def new_chat_create_app_g1():
    form = ChatFormUpdate()
    if form.validate_on_submit():
        chat = Chat(title=form.title.data, content=form.content.data, author=current_user, chat_module='App Module Chat',
                     chat_group='Group 1')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('chats.chat_web'))
    return render_template('chat/create_chat_app_g1.html', title='Create Chat', form=form, legend='App Module Chat, Group 1',
                           paragraph='Moni (Monica), KieranClark, Solveig, Kleppe (Peder), Rebecca, ethan.mcchristian, Ivanessa, Katharina, Hala')

@chats.route("/chat_new/create/app_g2", methods=['GET', 'POST'])
@login_required
def new_chat_create_app_g2():
    form = ChatFormUpdate()
    if form.validate_on_submit():
        chat = Chat(title=form.title.data, content=form.content.data, author=current_user, chat_module='App Module Chat',
                     chat_group='Group 2')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('chats.chat_web'))
    return render_template('chat/create_chat_app_g3.html', title='Create Chat', form=form, legend='App Module Chat, Group 2',
                           paragraph='Veronika, csalvati (Cristina), Krossland (Kristian), elizaveta.goncharova, Sabrina, Steffen, Vanessa, Axel')

@chats.route("/chat_new/create/app_g3", methods=['GET', 'POST'])
@login_required
def new_chat_create_app_g3():
    form = ChatFormUpdate()
    if form.validate_on_submit():
        chat = Chat(title=form.title.data, content=form.content.data, author=current_user, chat_module='App Module Chat',
                     chat_group='Group 3')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('chats.chat_web'))
    return render_template('chat/create_chat_app_g3.html', title='Create Chat', form=form, legend='App Module Chat, Group 3',
                           paragraph='Marita, Paula, paolo rossi, runar_johnston, Louise, mitcht (Mitchell), Klara, Yasmina')

@chats.route("/chat_new/create/app_g4", methods=['GET', 'POST'])
@login_required
def new_chat_create_app_g4():
    form = ChatFormUpdate()
    if form.validate_on_submit():
        chat = Chat(title=form.title.data, content=form.content.data, author=current_user, chat_module='App Module Chat',
                     chat_group='Group 4')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('chats.chat_web'))
    return render_template('chat/create_chat_app_g4.html', title='Create Chat', form=form, legend='App Module Chat, Group 4',
                           paragraph='Seb (Sebastian), Leonora Skorpen, conte, fabian, Marthine, FilipF, Tiphaine, Igor, Marius')

@chats.route("/chat_new/create/app_g5", methods=['GET', 'POST'])
@login_required
def new_chat_create_app_g5():
    form = ChatFormUpdate()
    if form.validate_on_submit():
        chat = Chat(title=form.title.data, content=form.content.data, author=current_user, chat_module='App Module Chat',
                     chat_group='Group 5')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('chats.chat_web'))
    return render_template('chat/create_chat_app_g5.html', title='Create Chat', form=form, legend='App Module Chat, Group 5',
                           paragraph='Ruth, ashish.kumar, marfjo (Maria), Marenoj (Maren), petnyg (Petter), Addison Liandong Wu, Mokhinur, Jon Heine, Kristoffer Jansen')

@chats.route("/chat_new/create/se_g1", methods=['GET', 'POST'])
@login_required
def new_chat_create_se_g1():
    form = ChatFormUpdate()
    if form.validate_on_submit():
        chat = Chat(title=form.title.data, content=form.content.data, author=current_user, chat_module='Sustainable Energy Module Chat',
                     chat_group='Group 1')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('chats.chat_web'))
    return render_template('chat/create_chat_se_g1.html', title='Create Chat', form=form, legend='Sustainable Energy Module Chat, Group 1',
                           paragraph1='Fabion Abazaj, Liandong Wu, Kristian Sj??en Rossland, Maren Johansen ??yan, Marthine Hjart??ker Ingebrigtsen, Petter Sveen Nygaard',
                           paragraph2='Nuclear energy and Renewable Energy Sources')


@chats.route("/chat_new/create/se_g2", methods=['GET', 'POST'])
@login_required
def new_chat_create_se_g2():
    form = ChatFormUpdate()
    if form.validate_on_submit():
        chat = Chat(title=form.title.data, content=form.content.data, author=current_user, chat_module='Sustainable Energy Module Chat',
                     chat_group='Group 2')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('chats.chat_web'))
    return render_template('chat/create_chat_se_g2.html', title='Create Chat', form=form, legend='Sustainable Energy Module Chat, Group 2',
                           paragraph1='Runar Hauk??s Johnston, Elizaveta Goncharova, Sebastian Bergseth, Veronika Priakhina, Louise Nicolini, Agathe Brattaule',
                           paragraph2='Political gender balance effect on renewables in the energy mix')

@chats.route("/chat_new/create/se_g3", methods=['GET', 'POST'])
@login_required
def new_chat_create_se_g3():
    form = ChatFormUpdate()
    if form.validate_on_submit():
        chat = Chat(title=form.title.data, content=form.content.data, author=current_user, chat_module='Sustainable Energy Module Chat',
                     chat_group='Group 3')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('chats.chat_web'))
    return render_template('chat/create_chat_se_g3.html', title='Create Chat', form=form, legend='Sustainable Energy Module Chat, Group 3',
                           paragraph1='Paolo Rossi, Sabrina Hartenfels, Vanessa Wickel, Paula Jimenez Gomez, Klara Wolschlager',
                           paragraph2='Tidal energy')

@chats.route("/chat_new/create/se_g4", methods=['GET', 'POST'])
@login_required
def new_chat_create_se_g4():
    form = ChatFormUpdate()
    if form.validate_on_submit():
        chat = Chat(title=form.title.data, content=form.content.data, author=current_user, chat_module='Sustainable Energy Module Chat',
                     chat_group='Group 4')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('chats.chat_web'))
    return render_template('chat/create_chat_se_g4.html', title='Create Chat', form=form, legend='Sustainable Energy Module Chat, Group 4',
                           paragraph1='Hala Al Jamal, Cristina Salvati, Ivanessa Staykova, Keiran Clark, Monica Schwartzel, Peder Sebastian Kleppe',
                           paragraph2='Energy storage and its interplay with the mining and sustainable energy industries')

@chats.route("/chat_new/create/se_g5", methods=['GET', 'POST'])
@login_required
def new_chat_create_se_g5():
    form = ChatFormUpdate()
    if form.validate_on_submit():
        chat = Chat(title=form.title.data, content=form.content.data, author=current_user, chat_module='Sustainable Energy Module Chat',
                     chat_group='Group 5')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('chats.chat_web'))
    return render_template('chat/create_chat_se_g5.html', title='Create Chat', form=form, legend='Sustainable Energy Module Chat, Group 5',
                           paragraph1='Steffen Nathan, Maria Sels??s, Ashish Kumar, Leopold Reinisch, Jon Heine, Filip Fandel',
                           paragraph2='Agrivoltaics -The use of croplands for both agriculture and solar energy at the same time')

@chats.route("/chat_new/create/se_g6", methods=['GET', 'POST'])
@login_required
def new_chat_create_se_g6():
    form = ChatFormUpdate()
    if form.validate_on_submit():
        chat = Chat(title=form.title.data, content=form.content.data, author=current_user, chat_module='Sustainable Energy Module Chat',
                     chat_group='Group 6')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('chats.chat_web'))
    return render_template('chat/create_chat_se_g6.html', title='Create Chat', form=form, legend='Sustainable Energy Module Chat, Group 6',
                           paragraph1='Axel ??stby, Leonora Leine Skorpen, Marius Slette, Kristoffer Jansen',
                           paragraph2='...')

@chats.route("/chat/<int:chat_id>")
def chat(chat_id):
    chat = Chat.query.get_or_404(chat_id)
    return render_template('chat/chat.html', title=chat.title, chat=chat, func=read_image)

@chats.route("/chat/<int:chat_id>/update", methods=['GET', 'POST'])
@login_required
def update_chat(chat_id):
    chat = Chat.query.get_or_404(chat_id)
    if chat.author != current_user:
        abort(403)
    form = ChatFormUpdate()
    if form.validate_on_submit():
        chat.title = form.title.data
        chat.content = form.content.data
        db.session.commit()
        flash('Your chat has been updated!', 'success')
        return redirect(url_for('chats.chat', chat_id=chat.id))
    elif request.method == 'GET':
        form.title.data = chat.title
        form.content.data = chat.content
    return render_template('chat/create_chat_lecture.html', title='Update chat',
                           form=form, legend='Update chat')

@chats.route("/chat/<int:chat_id>/delete", methods=['GET', 'POST'])
@login_required
def delete_chat(chat_id):
    chat = Chat.query.get_or_404(chat_id)
    if chat.author != current_user:
        abort(403)
    db.session.delete(chat)
    db.session.commit()
    flash('Your chat has been deleted!', 'success')
    return redirect(url_for('chats.chat_web'))

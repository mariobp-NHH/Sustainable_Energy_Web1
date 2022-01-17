import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from webse import app, db, bcrypt, test_post, test_announcement
from webse.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm, AppStatisticsForm, SEStatisticsForm, AnnouncementForm
from webse.forms import ModulsForm_M1_Ch2_Q1, ModulsForm_M1_Ch2_Q2, ModulsForm_M1_Ch2_Q3, ModulsForm_M1_Ch2_Q4, ModulsForm_M1_Ch2_Q5
from webse.forms import ModulsForm_M1_Ch1_Q1, ModulsForm_M1_Ch1_Q2, ModulsForm_M1_Ch1_Q3
from webse.forms import ModulsForm_M2_Ch1_Q1, ModulsForm_M2_Ch1_Q2, ModulsForm_M2_Ch1_Q3
from webse.forms import ModulsForm_M2_Ch2_Q1, ModulsForm_M2_Ch2_Q2, ModulsForm_M2_Ch2_Q3
from webse.models import User, Post, Moduls, Announcement, PostG
from flask_login import login_user, current_user, logout_user, login_required

@app.before_first_request
def before_first_request():
    db.create_all()

@app.route('/home')
@app.route('/')
def home():
    if test_announcement:
        total_pages_announcements = Announcement.query.count()
        max_pages_announcements = Announcement.query.count()
    else:
        total_pages_announcements=0
        max_pages_announcements = 0
    if test_post:
        
        total_pages_posts = Post.query.count()
        max_pages_posts = Post.query.count()/2
    else:
        total_pages_posts = 0
        max_pages_posts = 0
    total_pages = min (total_pages_announcements, total_pages_posts)
    
    max_pages=max(max_pages_announcements,max_pages_posts)
    min_pages = min(max_pages_announcements, max_pages_posts)
    page = request.args.get('page', 1, type=int)
    """
    if total_pages<page:
        announcements = Announcement.query.all()
        posts = Post.query.all()
    elif total_pages_announcements<page and total_pages_posts>=page:
        announcements = Announcement.query.all()
        posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=2)
    elif total_pages_announcements>=page and total_pages_posts<page:
        announcements = Announcement.query.order_by(Announcement.date_posted.desc()).paginate(page=page, per_page=1)
        posts = Post.query.all()
        """
    
    if test_announcement:
        if page<=min_pages:
            announcements = Announcement.query.order_by(Announcement.date_posted.desc()).paginate(page=page, per_page=1)
        elif page>min_pages and max_pages>=page>max_pages_posts:
            announcements = Announcement.query.order_by(Announcement.date_posted.desc()).paginate(page=page, per_page=1)
        else:
            announcements = Announcement.query.order_by(Announcement.date_posted.desc()).paginate(page=max_pages_announcements, per_page=1)
    else:
        announcements=None
	
    if test_post:
        if page<=min_pages:
            posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=2)
        elif page>min_pages and max_pages>=page>max_pages_posts:
            posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=max_pages_posts, per_page=2)
        else:
            posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=2)
    else:
        posts=None
	
    return render_template('home.html', posts=posts, announcements=announcements, title='Home',
                           total_pages_announcements=total_pages_announcements, total_pages_posts=total_pages_posts)

@app.route('/chat_post_w')
@login_required
def chat_post_w():
    page = request.args.get('page', 1, type=int)
    group = current_user.group
    posts = PostG.query.filter_by(group=current_user.group).order_by(PostG.date_posted.desc()).paginate(page=page, per_page=2)

    return render_template('chat_post_w.html', posts=posts, group=group)


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    moduls = Moduls.query.all()
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.group = form.group.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account',
                           image_file=image_file, form=form, moduls=moduls)

#Chat-Posts functions
@app.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('create_post.html', title='New Chat-Post',
                           form=form, legend='New Chat-Post')

@app.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)

@app.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post',
                           form=form, legend='Update Post')

@app.route("/post/<int:post_id>/delete", methods=['GET', 'POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('home'))

@app.route("/user/<string:username>")
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=4)
    return render_template('user_posts.html', posts=posts, user=user)

#Chat-Posts-Group functions
@app.route("/post-group/new", methods=['GET', 'POST'])
@login_required
def new_post_g():
    form = PostForm()
    if form.validate_on_submit():
        post = PostG(title=form.title.data, content=form.content.data, author=current_user, group=current_user.group)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('chat_post_w'))
    return render_template('create_post_g.html', title='New Chat-Post-Group',
                           form=form, legend='New Chat-Post (Group)')

@app.route("/post-group/<int:post_id>")
def post_g(post_id):
    post = PostG.query.get_or_404(post_id)
    return render_template('post_g.html', title=post.title, post=post)

@app.route("/post-group/user/<string:username>")
def user_posts_g(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = PostG.query.filter_by(author=user)\
        .order_by(PostG.date_posted.desc())\
        .paginate(page=page, per_page=4)
    return render_template('user_posts_g.html', posts=posts, user=user)

@app.route("/post-group/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post_g(post_id):
    post = PostG.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('post_g', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post_g.html', title='Update Post',
                           form=form, legend='Update Post')

@app.route("/post-group/<int:post_id>/delete", methods=['GET', 'POST'])
@login_required
def delete_post_g(post_id):
    post = PostG.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('chat_post_w'))

#Announcements functions
@app.route("/announcement/new", methods=['GET', 'POST'])
@login_required
def new_announcement():
    form = AnnouncementForm()
    if form.validate_on_submit():
        announcement = Announcement(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(announcement)
        db.session.commit()
        flash('Your announcement has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('create_announcement.html', title='New Announcement',
                           form=form, legend='New Announcement')

@app.route("/announcement/<int:announcement_id>")
def announcement(announcement_id):
    announcement = Announcement.query.get_or_404(announcement_id)
    return render_template('announcement.html', title=announcement.title, announcement=announcement)

@app.route("/announcement/user/<string:username>")
def user_announcements(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    announcements = Announcement.query.filter_by(author=user)\
        .order_by(Announcement.date_posted.desc())\
        .paginate(page=page, per_page=4)
    return render_template('user_announcements.html', announcements=announcements, user=user)

@app.route("/announcement/<int:announcement_id>/update", methods=['GET', 'POST'])
@login_required
def update_announcement(announcement_id):
    announcement = Announcement.query.get_or_404(announcement_id)
    if announcement.author != current_user:
        abort(403)
    form = AnnouncementForm()
    if form.validate_on_submit():
        announcement.title = form.title.data
        announcement.content = form.content.data
        db.session.commit()
        flash('Your announcement has been updated!', 'success')
        return redirect(url_for('announcement', announcement_id=announcement.id))
    elif request.method == 'GET':
        form.title.data = announcement.title
        form.content.data = announcement.content
    return render_template('create_announcement.html', title='Update Announcement',
                           form=form, legend='Update Announcement')


@app.route("/announcement/<int:announcement_id>/delete", methods=['GET', 'POST'])
@login_required
def delete_announcement(announcement_id):
    announcement = Announcement.query.get_or_404(int(announcement_id))
    if announcement.author != current_user:
        abort(403)
    db.session.delete(announcement)
    db.session.commit()
    flash('Your announcement has been deleted!', 'success')
    return redirect(url_for('home'))

# App Calculator form
@app.route('/app_calculator')
def app_calculator():
	return render_template('app_calculator.html', title='App Calculator')

# App Calculator routine
@app.route('/send1', methods=['POST'])
def send(sum=sum):
	num1 = request.form.get("num1")
	num2 = request.form.get("num2")
	oper_name = request.form.get("operation")

	num1 = float(num1)
	num2 = float(num2)
	if oper_name == "add":
		oper_result = num1 + num2
	elif oper_name == "subtract":
		oper_result = num1 - num2
	elif oper_name == "multiply":
		oper_result = num1 * num2
	elif oper_name == "divide":
		oper_result = num1 / num2

	return render_template ('app_calculator.html', sum=oper_result)


@app.route('/teachers')
def teachers():
	return render_template('teachers.html', title='Teachers')


# App web
@app.route('/app_web')
@login_required
def app_web():
	return render_template('app web/app_web.html', title='App Web')


# Sustainable Energy Web
@app.route('/sustainable_energy_web')
@login_required
def sustainable_energy_web():
	return render_template('se web/sustainable_energy_web.html', title='SE Web')

# App Module, Chapter 1.
@app.route('/app_web/ch1', methods=['GET', 'POST'])
@login_required
def app_web_ch1():
    form_M1_Ch1_Q1 = ModulsForm_M1_Ch1_Q1()
    form_M1_Ch1_Q2 = ModulsForm_M1_Ch1_Q2()
    form_M1_Ch1_Q3 = ModulsForm_M1_Ch1_Q3()

    if form_M1_Ch1_Q1.validate_on_submit():
        Moduls.query.filter_by(author=current_user).\
            filter(Moduls.title_mo.is_('App Development')).\
            filter(Moduls.title_ch.is_('Ch1. Introduction')).\
            filter(Moduls.question_num.is_(1)).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_M1_Ch1_Q1.type.data, author=current_user)
        if moduls.question_str == 'Python':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'App Development'
        moduls.title_ch = 'Ch1. Introduction'
        moduls.question_num = 1
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('app_web_ch1'))

    if form_M1_Ch1_Q2.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo.is_('App Development')). \
            filter(Moduls.title_ch.is_('Ch1. Introduction')). \
            filter(Moduls.question_num.is_(2)).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_M1_Ch1_Q2.type.data, author=current_user)
        if moduls.question_str == 'GitHub':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'App Development'
        moduls.title_ch = 'Ch1. Introduction'
        moduls.question_num = 2
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('app_web_ch1'))

    if form_M1_Ch1_Q3.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo.is_('App Development')). \
            filter(Moduls.title_ch.is_('Ch1. Introduction')). \
            filter(Moduls.question_num.is_(3)).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_M1_Ch1_Q3.type.data, author=current_user)
        if moduls.question_str == 'Easy':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'App Development'
        moduls.title_ch = 'Ch1. Introduction'
        moduls.question_num = 3
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('app_web_ch1'))

    return render_template('app web/app_web_ch1.html', title='App Web - Ch1',
                           form_M1_Ch1_Q1=form_M1_Ch1_Q1, form_M1_Ch1_Q2=form_M1_Ch1_Q2,
                           form_M1_Ch1_Q3=form_M1_Ch1_Q3)

# App Module, Chapter 2.
@app.route('/app_web/ch2', methods=['GET', 'POST'])
@login_required
def app_web_ch2():
    form_M1_Ch2_Q1 = ModulsForm_M1_Ch2_Q1()
    form_M1_Ch2_Q2 = ModulsForm_M1_Ch2_Q2()
    form_M1_Ch2_Q3 = ModulsForm_M1_Ch2_Q3()
    form_M1_Ch2_Q4 = ModulsForm_M1_Ch2_Q4()
    form_M1_Ch2_Q5 = ModulsForm_M1_Ch2_Q5()

    if form_M1_Ch2_Q1.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo.is_('App Development')). \
            filter(Moduls.title_ch.is_('Ch2. Installation')). \
            filter(Moduls.question_num.is_(1)).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_M1_Ch2_Q1.question_str.data, author=current_user)
        if moduls.question_str == 'yes':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'App Development'
        moduls.title_ch = 'Ch2. Installation'
        moduls.question_num = 1
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('app_web_ch2'))

    if form_M1_Ch2_Q2.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo.is_('App Development')). \
            filter(Moduls.title_ch.is_('Ch2. Installation')). \
            filter(Moduls.question_num.is_(2)).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_M1_Ch2_Q2.type.data, author=current_user)
        if moduls.question_str == 'wind':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'App Development'
        moduls.title_ch = 'Ch2. Installation'
        moduls.question_num = 2
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('app_web_ch2'))

    if form_M1_Ch2_Q3.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo.is_('App Development')). \
            filter(Moduls.title_ch.is_('Ch2. Installation')). \
            filter(Moduls.question_num.is_(3)).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_M1_Ch2_Q3.type.data, author=current_user)
        if moduls.question_str == 'income':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'App Development'
        moduls.title_ch = 'Ch2. Installation'
        moduls.question_num = 3
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('app_web_ch2'))

    if form_M1_Ch2_Q4.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo.is_('App Development')). \
            filter(Moduls.title_ch.is_('Ch2. Installation')). \
            filter(Moduls.question_num.is_(4)).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_M1_Ch2_Q4.type.data, author=current_user)
        if moduls.question_str == 'school':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'App Development'
        moduls.title_ch = 'Ch2. Installation'
        moduls.question_num = 4
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('app_web_ch2'))

    if form_M1_Ch2_Q5.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo.is_('App Development')). \
            filter(Moduls.title_ch.is_('Ch2. Installation')). \
            filter(Moduls.question_num.is_(5)).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_M1_Ch2_Q5.type.data, author=current_user)
        if moduls.question_str == 'Hydrogen':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'App Development'
        moduls.title_ch = 'Ch2. Installation'
        moduls.question_num = 5
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('app_web_ch2'))

    return render_template('app web/app_web_ch2.html', title='App Web - Ch2',
                           form_M1_Ch2_Q1=form_M1_Ch2_Q1, form_M1_Ch2_Q2=form_M1_Ch2_Q2, form_M1_Ch2_Q3 = form_M1_Ch2_Q3,
                           form_M1_Ch2_Q4=form_M1_Ch2_Q4, form_M1_Ch2_Q5=form_M1_Ch2_Q5)

# Sustainable Energy Module, Chapter 1.
@app.route('/sustainable_energy_web/ch1', methods=['GET', 'POST'])
@login_required
def se_web_ch1():
    form_M2_Ch1_Q1 = ModulsForm_M2_Ch1_Q1()
    form_M2_Ch1_Q2 = ModulsForm_M2_Ch1_Q2()
    form_M2_Ch1_Q3 = ModulsForm_M2_Ch1_Q3()

    if form_M2_Ch1_Q1.validate_on_submit():
        Moduls.query.filter_by(author=current_user).\
            filter(Moduls.title_mo.is_('Sustainable Energy')).\
            filter(Moduls.title_ch.is_('Ch1. Overview')).\
            filter(Moduls.question_num.is_(1)).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_M2_Ch1_Q1.type.data, author=current_user)
        if moduls.question_str == 'Africa':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch1. Overview'
        moduls.question_num = 1
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_web_ch1'))

    if form_M2_Ch1_Q2.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo.is_('Sustainable Energy')). \
            filter(Moduls.title_ch.is_('Ch1. Overview')). \
            filter(Moduls.question_num.is_(2)).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_M2_Ch1_Q2.type.data, author=current_user)
        if moduls.question_str == 'Local':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch1. Overview'
        moduls.question_num = 2
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_web_ch1'))

    if form_M2_Ch1_Q3.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo.is_('Sustainable Energy')). \
            filter(Moduls.title_ch.is_('Ch1. Overview')). \
            filter(Moduls.question_num.is_(3)).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_M2_Ch1_Q3.type.data, author=current_user)
        if moduls.question_str == 'Medium':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch1. Overview'
        moduls.question_num = 3
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_web_ch1'))
    return render_template('se web/se_web_ch1.html', title='SE Web - Ch1',
                           form_M2_Ch1_Q1=form_M2_Ch1_Q1, form_M2_Ch1_Q2=form_M2_Ch1_Q2,
                           form_M2_Ch1_Q3=form_M2_Ch1_Q3)

# Sustainable Energy Module, Chapter 2.
@app.route('/sustainable_energy_web/ch2', methods=['GET', 'POST'])
@login_required
def se_web_ch2():
    form_M2_Ch2_Q1 = ModulsForm_M2_Ch2_Q1()
    form_M2_Ch2_Q2 = ModulsForm_M2_Ch2_Q2()
    form_M2_Ch2_Q3 = ModulsForm_M2_Ch2_Q3()

    if form_M2_Ch2_Q1.validate_on_submit():
        Moduls.query.filter_by(author=current_user).\
            filter(Moduls.title_mo.is_('Sustainable Energy')).\
            filter(Moduls.title_ch.is_('Ch2. Wind')).\
            filter(Moduls.question_num.is_(1)).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_M2_Ch2_Q1.type.data, author=current_user)
        if moduls.question_str == 'Africa':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch2. Wind'
        moduls.question_num = 1
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_web_ch2'))

    if form_M2_Ch2_Q2.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo.is_('Sustainable Energy')). \
            filter(Moduls.title_ch.is_('Ch2. Wind')). \
            filter(Moduls.question_num.is_(2)).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_M2_Ch2_Q2.type.data, author=current_user)
        if moduls.question_str == 'Local':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch2. Wind'
        moduls.question_num = 2
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_web_ch2'))

    if form_M2_Ch2_Q3.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo.is_('Sustainable Energy')). \
            filter(Moduls.title_ch.is_('Ch2. Wind')). \
            filter(Moduls.question_num.is_(3)).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_M2_Ch2_Q3.type.data, author=current_user)
        if moduls.question_str == 'Medium':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch2. Wind'
        moduls.question_num = 3
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_web_ch2'))
    return render_template('se web/se_web_ch2.html', title='SE Web - Ch2',
                           form_M2_Ch2_Q1=form_M2_Ch2_Q1, form_M2_Ch2_Q2=form_M2_Ch2_Q2,
                           form_M2_Ch2_Q3=form_M2_Ch2_Q3)



@app.route('/about' )
def about():
    return render_template('about.html')

@app.route('/ciao' )
def ciao():
    entries = []
    return redirect(url_for('statistics', entries=entries))

#Statistics
@app.route('/statistics', methods=['GET', 'POST'])
@login_required
def statistics():
    app_statistics_form = AppStatisticsForm()
    se_statistics_form = SEStatisticsForm()
    if app_statistics_form.validate_on_submit():
        app_statistics_input = app_statistics_form.type.data
        entries_app = Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo.is_('App Development')). \
            filter(Moduls.title_ch.is_(app_statistics_input)). \
            order_by(Moduls.question_num.asc()).all()

        app_incorrect = Moduls.query.filter_by(author=current_user). \
            filter(Moduls.question_result.is_(0)). \
            filter(Moduls.title_mo.is_('App Development')). \
            filter(Moduls.title_ch.is_(app_statistics_input)). \
            order_by(Moduls.question_num.asc()).count()

        app_correct = Moduls.query.filter_by(author=current_user). \
            filter(Moduls.question_result.is_(1)). \
            filter(Moduls.title_mo.is_('App Development')). \
            filter(Moduls.title_ch.is_(app_statistics_input)). \
            order_by(Moduls.question_num.asc()).count()

        flash('Your answer has been submitted!', 'success')
        return render_template('statistics2.html', app_statistics_form=app_statistics_form,
                               se_statistics_form=se_statistics_form, entries_app=entries_app,
                               app_correct=app_correct, app_incorrect=app_incorrect,
                               se_correct=0, se_incorrect=0)
    if se_statistics_form.validate_on_submit():
        se_statistics_input = se_statistics_form.type.data
        entries_se = Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo.is_('Sustainable Energy')). \
            filter(Moduls.title_ch.is_(se_statistics_input)). \
            order_by(Moduls.question_num.asc()).all()

        se_incorrect = Moduls.query.filter_by(author=current_user). \
            filter(Moduls.question_result.is_(0)). \
            filter(Moduls.title_mo.is_('Sustainable Energy')). \
            filter(Moduls.title_ch.is_(se_statistics_input)). \
            order_by(Moduls.question_num.asc()).count()

        se_correct = Moduls.query.filter_by(author=current_user). \
            filter(Moduls.question_result.is_(1)). \
            filter(Moduls.title_mo.is_('Sustainable Energy')). \
            filter(Moduls.title_ch.is_(se_statistics_input)). \
            order_by(Moduls.question_num.asc()).count()

        flash('Your answer has been submitted!', 'success')
        return render_template('statistics2.html', app_statistics_form=app_statistics_form,
                               se_statistics_form=se_statistics_form, entries_se=entries_se,
                               app_correct=0, app_incorrect=0,
                               se_correct=se_correct, se_incorrect=se_incorrect)

    entries_app = Moduls.query.filter_by(author=current_user).filter(Moduls.title_mo.is_('---')).order_by(Moduls.date_exercise.desc()).all()
    entries_se = Moduls.query.filter_by(author=current_user).filter(Moduls.title_mo.is_('---')).order_by(
        Moduls.date_exercise.desc()).all()
    return render_template('statistics2.html', app_statistics_form=app_statistics_form, se_statistics_form=se_statistics_form,
                           entries_app=entries_app, entries_se=entries_se,
                               app_correct=0, app_incorrect=0,
                               se_correct=0, se_incorrect=0)




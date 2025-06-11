from flask import Blueprint, render_template, redirect, url_for, flash, request, abort
from models import db, Post
from forms import PostForm
from flask_login import current_user, login_required

blog_bp = Blueprint('blog', __name__)

@blog_bp.route('/')
def home():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template('home.html', posts=posts)

@blog_bp.route('/post/new', methods=['GET', 'POST'])
@login_required
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(
            title=form.title.data,
            content=form.content.data,
            author=current_user
        )
        db.session.add(post)
        db.session.commit()
        flash("Post yaratildi!", "success")
        return redirect(url_for('blog.home'))
    return render_template('create_post.html', form=form)

@blog_bp.route('/post/<int:post_id>')
def post_detail(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post_detail.html', post=post)

@blog_bp.route('/post/<int:post_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm(obj=post)
    if form.validate_on_submit():
        post.title   = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash("Post yangilandi!", "success")
        return redirect(url_for('blog.post_detail', post_id=post.id))
    return render_template('create_post.html', form=form)

@blog_bp.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash("Post o‘chirildi!", "success")
    return redirect(url_for('blog.home'))

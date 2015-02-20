from flask import render_template, abort, url_for, redirect, request
from app import app, db
from app.models import Poll
from app.forms import CreatePoll
from json import loads, dumps

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/new", methods=["GET", "POST"])
def new():
    create_poll = CreatePoll()
    if create_poll.validate_on_submit():
        votes_list = {}
        for option in create_poll.options.data.split("\n"):
            votes_list[option.strip("\r")] = 0
        create_poll.options.data.strip("\r")
        new_poll = Poll(title=create_poll.title.data,
                        options=dumps(create_poll.options.data.splitlines()),
                        votes=dumps(votes_list))
        db.session.add(new_poll)
        db.session.commit()
        return redirect(url_for("poll", identifier=Poll.query.filter_by(title=create_poll.title.data).first().id))
    return render_template("new.html", form=create_poll)


@app.route("/poll/<identifier>", methods=["GET", "POST"])
def poll(identifier):
    poll_obj = Poll.query.filter_by(id=identifier).first()
    if poll_obj is None:
        abort(404)
    if request.method == "POST":
        current_poll = Poll.query.filter_by(id=identifier).first()
        current_votes = loads(current_poll.votes)
        current_votes[request.form["option"]] += 1
        current_poll.votes = dumps(current_votes)
        db.session.add(current_poll)
        db.session.commit()
        return redirect(url_for("results", identifier=identifier))
    else:
        return render_template("poll.html", poll=poll_obj)


@app.route("/poll/<identifier>/results")
def results(identifier):
    poll_obj = Poll.query.filter_by(id=identifier).first()
    if poll_obj is None:
        abort(404)
    total = 0
    votes = loads(poll_obj.votes)
    for i in votes:
        total += int(votes[i])
    bars = {}
    for i in votes:
        try:
            bars[i] = int((votes[i] / total) * 100)
        except ZeroDivisionError:
            bars[i] = 0
    return render_template("results.html", bars=bars, poll=poll_obj)


@app.route("/listpolls")
def list_polls():
    return render_template("listpolls.html", polls=Poll.query.all())


@app.route("/poll/<identifier>/results/json")
def results_json(identifier):
    pass
    poll_obj = Poll.query.filter_by(id=identifier).first()
    if poll_obj is None:
        abort(404)
    total = 0
    votes = loads(poll_obj.votes)
    for i in votes:
        total += int(votes[i])
    bars = {}
    for i in votes:
        try:
            bars[i] = int((votes[i] / total) * 100)
        except ZeroDivisionError:
            bars[i] = 0
    return dumps(bars)
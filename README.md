# ABOUT THIS BRANCH

I started implementing the screenshot bot as a dockerized service. I also
started changing the screenshot bot to use headless firefox instead of headless
chrome because firefox has lower system requirements.

### _however_

I realized that a selenium-browser based screenshotting mechanism will always
be too costly. Capturing, storing, and distributing screenshots requires a
lot of infrastructure, and the goal is to serve this website as cheaply as
possible so that it is as available to teachers as possible.

Therefore, I'm suspending development towards this screenshoting mechanism
and working on a midi parser instead.

I'm creating this branch to save my progress since the firefox screenshotting
mechanism is almost fully implemented. I got all the tests to pass once, but
for some reason the docker container isn't currently building. Theoretically,
if the docker container builds, the tests will pass and the screenshotter will
work.


# Welcome to the Music Lab Song Maker Gallery!

This website was created by me, a music teacher, in response to the simple
need to find a way to feature our students' work in light of the COVID-19
pandemic. Our students' concerts have been cancelled, their rehearsals ceased,
and their opportunities to share music diminished to a whisper of what they
once were.

As a third, fourth, and fifth grade elementary general music teacher, a big
part of my COVID curriculum has been the Chrome Music Lab. Students love
making creations with it; it's fun and easy to use, and it provides an
amazing platform for us to discuss the topics in our music curriculum. For me,
the music lab has been an indispensable tool for coping with our school
closure.

This website is a simple way to share your students' work with your whole
community. I know that I have been awestruck by the creativity of many of the
music lab compositions that my students have shared with me, and I am sure
that you feel the same.

## We need a beautiful, simple, and easy way to share these compositions with
## as many people as possible!

# How it Works

The teacher posts links from
[this website](http://musiclab.chromeexperiments.com/Song-Maker/).
The site takes screenshots of student work, and displays them as thumbnails
in a public gallery, displaying student work in a beautiful visual format.


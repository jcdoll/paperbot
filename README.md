## paperbot
Submit links, download papers.

Intended for personal use on a private network. Allows a single authorized user to easily access papers from multiple computers without repeated authentication. Sharing of documents with unauthorized users is strictly prohibited by most journals.

Assumes proxy-based access to scientific journals, commonly provided through an employer or academic institution.

## status
Currently a non-functional side project.

## run instructions
1. Install VirtualBox: virtualbox.org/wiki/Downloads
2. Install Vagrant: vagrantup.com/downloads.html
3. Run 'vagrant up' from your favorite shell. Wait a few minutes.
4. Access paperbot @ localhost:5000.

Built on Flask, Docker and Vagrant for portability.

## dev tips
1. vagrant up && vagrant ssh
2. Container terminal: docker exec -it paperbot bash
3. Monitoring results: docker attach paperbot

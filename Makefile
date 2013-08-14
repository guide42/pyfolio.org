build:
	python folioweb.py
upload: build
	rsync -e "ssh -p 443" -P -rvz --delete build/* momo.guide42.com:/srv/www/pyfolio.org
clean:
	rm -rf build/

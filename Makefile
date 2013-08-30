build:
	python folioweb.py
run: build
	python run.py
upload: build
	rsync -e "ssh -p 443" -P -rvz --delete build/* momo.guide42.com:/srv/www/pyfolio.org
clean:
	rm -rf build/

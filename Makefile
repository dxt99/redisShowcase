server:
	python3 src/server.py

clients:
	(python3 src/client.py >> client.txt)&(python3 src/listener.py >> listener.txt)

clean: clean-db clean-output

clean-db:
	redis-cli FLUSHALL

clean-output:
	rm -f listener.txt
	rm -f client.txt
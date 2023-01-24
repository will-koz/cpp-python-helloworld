all:
	./build.py build
	cp build/*/*.so .

clean:
	rm -rf __pycache__/ build/
	rm -rf *.so *.o

.PHONY: all clean

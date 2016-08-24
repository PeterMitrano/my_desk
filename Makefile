all: zip upload

zip:
	mkdir -p build
	rm -f ./build/skill.zip
	cp -r ./lambda_function.py build
	cd build &&	zip -q -r skill.zip *

upload: zip
	aws lambda update-function-code --function-name MyDesk --zip-file fileb://build/skill.zip
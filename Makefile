# https://aws.amazon.com/architecture/icons/
ICON_PACK = https://media.amazonwebservices.com/AWS-Design/Arch-Center/16.2.22_Update/AWS_Simple_Icons_EPS-SVG_v16.2.22.zip

help: ## Shows this help
	@echo "$$(grep -h '#\{2\}' $(MAKEFILE_LIST) | sed 's/: #\{2\} /	/' | column -t -s '	')"

clean:
	rm -rf build/ dist/ *.egg-info/

build: ## Build
build: clean icons

.PHONY: icons
icons: ## Get png icons into ./icons
	wget $(ICON_PACK) -O /tmp/aws_icons.zip
	# mkdir -p $@
	unzip -j /tmp/aws_icons.zip *.png -x */._* -d icons
	# Workaround for setup.py refusing to extract icons from package data
	touch icons/__init__.py

test:
	-pip uninstall terraform-aws-icons --yes
	pip install .
	cat examples/aws-asg.dot | terraform-iconify | dot -Tpng -o "examples/aws-asg.png"
	cat examples/aws-rds.dot | terraform-iconify | dot -Tpng -o "examples/aws-rds.png"

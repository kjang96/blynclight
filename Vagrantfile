ENV["VAGRANT_DEFAULT_PROVIDER"] = "virtualbox"

Vagrant.configure(2) do |config|

  config.vm.provider "virtualbox" do |vm|
    vm.linked_clone = true
    vm.customize ['modifyvm', :id, '--usb', 'on']
    vm.customize ['usbfilter', 'add', '0', '--target', :id, '--name', 'Blynclight', '--vendorid', '0x0e53', '--productid', '0x2516']
  end

  config.vm.network "forwarded_port", guest: 5000, host: 5000

  config.vm.define :blynclight do |system|
    system.vm.box = "boxcutter/ubuntu1604"
  end

  $script = <<SCRIPT
sudo apt-get update
sudo apt-get install -y python-setuptools python-dev build-essential
sudo easy_install pip
sudo pip install pyusb
sudo pip install Flask
SCRIPT

  config.vm.provision "shell", inline: $script
  config.vm.provision "shell", run: "always", privileged: false do |s|
    s.inline = "sudo python /vagrant/blynclight/server.py &"
  end
end

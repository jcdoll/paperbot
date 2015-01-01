# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"

  config.ssh.forward_agent = true
  config.vm.network "private_network", :ip => "172.16.1.10"
  config.vm.network "forwarded_port", guest: 5000, host: 5000
 
  config.vm.provision :shell, :path => 'script/provision'

  config.vm.provision "docker" do |d|
    d.build_image "/vagrant", args: "-t=paperbot"
    d.run "paperbot", image: "paperbot", args: "-p 5000:5000 -v /vagrant:/code"
  end
end

ENV["VAGRANT_DEFAULT_PROVIDER"] = "parallels"

Vagrant.configure(2) do |config|

  config.ssh.forward_agent = true

  config.vm.synced_folder ".", "/vagrant"

  config.vm.provider "parallels" do |vm|
    vm.linked_clone = true
    vm.update_guest_tools = true
  end

  # NOTE: test boxes obtained from https://atlas.hashicorp.com/boxcutter
  # packer build source repo: https://github.com/boxcutter

  config.vm.define :k8sclient do |system|
    system.vm.box = "boxcutter/ubuntu1604"
  end

end
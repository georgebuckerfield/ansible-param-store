# Ansible Lookup: AWS Parameter Store

An Ansible lookup plugin to retrieve parameters from AWS Parameter Store (part of EC2 Systems Manager).

## Usage

Place the plugin file in your plugins directory (see [here](https://docs.ansible.com/ansible/dev_guide/developing_plugins.html#distributing-plugins) for more information). Alternatively, create a directory called `lookup_plugins` in the root of your project and put the file there. The plugin will be automatically loaded by Ansible.

You can now use the plugin in your playbook:

```
- hosts: localhost
  vars:
    mysql_hostname: "{{ lookup('aws-param-store', 'mysql_hostname') }}"
    mysql_root_pw: "{{ lookup('aws-param-store', 'mysql_root_pw', decrypt=True) }}"
 
  tasks:
    - debug: msg="The hostname of the mysql instance is: {{ mysql_hostname }}"
    - debug: msg="The root password is: {{ mysql_root_pw }}"
 ```
 
 The `decrypt` option allows you to choose whether to decrypt parameters stored as secure strings. You will need the necessary IAM permissions to decrypt the parameter.

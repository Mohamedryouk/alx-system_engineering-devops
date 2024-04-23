# make changes to config file using Puppet

include stdlib
file { 'etc/ssh/ssh_config':
    ensure => present
}
file_line { 'Refuse to authenticate using a password':
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
  match  => '#PasswordAuthentication',
}

file_line { 'Use private key':
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile /.ssh/school'
  match  => 'IdentityFile',
}
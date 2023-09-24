# A script that using puppet to configure client ssh

exec {'echo':
  command => 'echo PasswordAuthentication no"\n"IdentityFile ~/.ssh/school >> /etc/ssh/ssh_config',
  path    => '/usr/bin'
}

# Change the OS configuration so that it is possible to
# login with the holberton user and open a file without any error message

exec { 'login_with_holberton':
  command  => 'sed -i "s/holberton hard nofile 5/holberton hard nofile 55000/g" /etc/security/limits.conf',
  provider => 'shell'
}

exec { 'login_with_holberton':
  command  => 'sed -i "s/holberton soft nofile 4/holberton soft nofile 55000/g" /etc/security/limits.conf',
  provider => 'shell'
}

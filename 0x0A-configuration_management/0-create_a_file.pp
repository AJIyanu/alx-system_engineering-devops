# Now create school under /tmp/

class file_creator {

  file { '/tmp/school':

    ensure => 'present',
    content => 'I love Puppet',
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0744',
    
  }

}

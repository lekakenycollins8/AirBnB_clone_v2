# Puppet manifest to set up web servers for deployment of web_static

# Update package repositories
package { 'nginx':
  ensure => 'installed',
}

# Create directories
file { ['/data/web_static/releases/test', '/data/web_static/shared']:
  ensure => 'directory',
}

# Create HTML file
file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  content => '<!DOCTYPE html>
              <html>
                  <head></head>
                  <body>
                      <h1>Hello World!</h1>
                      <p>This is a test page for nginx configuration</p>
                  </body>
              </html>',
}

# Set symbolic link
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
  force  => true,
}

# Set ownership
file { '/data':
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}

# Update nginx configuration
file_line { 'nginx_web_static_location':
  ensure => present,
  path   => '/etc/nginx/sites-enabled/default',
  line   => '        location /hbnb_static { alias /data/web_static/current/; }',
  match  => 'listen 80 default_server',
}

# Restart nginx service
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/etc/nginx/sites-enabled/default'],
}

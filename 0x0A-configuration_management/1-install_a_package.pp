# Install Flask the puppet way

package { 'Flask':
    ensure   => '2.2.2',
    provider => 'pip3',
}

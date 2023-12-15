# Let the puppet assasinate

exec { 'kill_killmenow_process':
    command => 'pkill -f killmenow',
    onlyif  => 'pgrep -f killmenow',
    path    => ['/bin', '/usr/bin'],
}

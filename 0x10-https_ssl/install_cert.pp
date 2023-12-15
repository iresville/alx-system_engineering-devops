# This puppet script installs certbot on servers: web-01, web-02, and lb-01
# www.iitsjason.tech points to 52.205.100.118
# lb-01.iitsjason.tech points to 52.205.100.118
# web-01.iitsjason.tech points to 18.204.5.218
# web-02.iitsjason.tech points to 52.205.100.118


node 'web-01.iitsjason.tech', 'web-02.iitsjason.tech', 'lb-01.iitsjason.tech' {
    package { 'certbot':
        ensure  => installed,
        version => '2.6.0',
    }
}

# Compléments à l'article MISC "Stocker ses secrets dans git, une mauvaise pratique pouvant avoir de lourdes conséquences"

## Génération de l'autorité de certification et des certificats

### Création de l'autorité de certification

```
openssl genrsa -des3 -out rootCA.key 4096
openssl req -x509 -new -nodes -key rootCA.key -sha256 -days 1024 -out rootCA.crt
```

### Création du certificat de Vault

```
openssl genrsa -out vaultApp.key 2048
openssl req -new -config tls_vault.conf -key vaultApp.key -out vaultApp.csr
openssl x509 -req -in vaultApp.csr -CA rootCA.crt -CAkey rootCA.key -CAcreateserial -out vaultApp.crt -days 500 -sha256 -extensions req_ext -extfile tls_vault.conf
```

### Création du certificat de l'application web

```
openssl genrsa -out webApp.key 2048
openssl req -new -config tls_web_app.conf -key webApp.key -out webApp.csr
openssl x509 -req -in webApp.csr -CA rootCA.crt -CAkey rootCA.key -CAcreateserial -out webApp.crt -days 500 -sha256
```

## Installation et lancement de Vault

Vault doit être installé en suivant les instructions correspondants au système d'exploitation utilisé : https://learn.hashicorp.com/tutorials/vault/getting-started-install?in=vault/getting-started

Lancer Vault

```
vault server -dev -config=vault_configuration.hcl
```


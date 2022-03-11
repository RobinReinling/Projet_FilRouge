FROM quay.io/keycloak/keycloak-x:latest as builder

ENV KC_METRICS_ENABLED=true
ENV KC_FEATURES=token-exchange
ENV KC_SCHEMA=bdd_projet
ENV KC_DB=mysql
RUN /opt/keycloak/bin/kc.sh build

FROM quay.io/keycloak/keycloak-x:latest
COPY --from=builder /opt/keycloak/lib/quarkus/ /opt/keycloak/lib/quarkus/
WORKDIR /opt/keycloak
# for demonstration purposes only, please make sure to use proper certificates in production instead
RUN keytool -genkeypair -storepass password -storetype PKCS12 -keyalg RSA -keysize 2048 -dname "CN=server" -alias server -ext "SAN:c=DNS:localhost,IP:127.0.0.1" -keystore conf/server.keystore
ENV KEYCLOAK_ADMIN=${KEYCLOAK_ADMIN}
ENV KEYCLOAK_ADMIN_PASSWORD=${KEYCLOAK_ADMIN_PASSWORD}
# change these values to point to a running postgres instance
ENV KC_DB_URL=jdbc:sqlserver://[bdd_projet:8080]
ENV KC_DB_USERNAME=root
ENV KC_DB_PASSWORD=root
ENV KC_HOSTNAME=localhost:8080
ENTRYPOINT ["/opt/keycloak/bin/kc.sh", "start"]
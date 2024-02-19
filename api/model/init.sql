CREATE TABLE network
(
    id         BIGSERIAL PRIMARY KEY,
    ip_addr    text               DEFAULT NULL,
    created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE network
(
    id         uuid      NOT NULL DEFAULT uuid_generate_v4() PRIMARY KEY,
    ip_addr    text               DEFAULT NULL,
    created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
);

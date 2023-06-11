CREATE TABLE IF NOT EXISTS user(
    id INTEGER PRIMARY KEY,
    public_id VARCHAR(36) NOT NULL,
    pseudonym VARCHAR(20) NOT NULL UNIQUE,
    email VARCHAR(75) NOT NULL UNIQUE,
    user_password VARCHAR(75) NOT NULL,
    registration_date DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS community(
    id INTEGER PRIMARY KEY,
    community_name VARCHAR(15) NOT NULL UNIQUE,
    public_id VARCHAR(36) NOT NULL,
    founder_id INTEGER NOT NULL,
    foundation_date DATE NOT NUll,
    community_description VARCHAR(500) NOT NULL,
    FOREIGN KEY (founder_id) REFERENCES user (id)
);

CREATE TABLE IF NOT EXISTS community_members(
    id INTEGER PRIMARY KEY,
    community_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (community_id) REFERENCES community (id),
    FOREIGN KEY (user_id) REFERENCES user (id)
);

CREATE TABLE IF NOT EXISTS post(
    id INTEGER PRIMARY KEY,
    owner_public_id VARCHAR(36) NOT NULL,
    public_id VARCHAR(36) NOT NULL,
    identified_public_id VARCHAR(36),
    community_public_id VARCHAR(36),
    post_description VARCHAR(500) NOT NULL,
    post_time TIMESTAMP NOT NUll,
    post_date DATE NOT NUll,
    post_type TEXT CHECK( post_type IN ('identified','community')),
    FOREIGN KEY (owner_public_id) REFERENCES user (public_id),
    FOREIGN KEY (identified_public_id) REFERENCES user (public_id),
    FOREIGN KEY (community_public_id) REFERENCES community (public_id)
);
CREATE TABLE IF NOT EXISTS post_interaction(
    id INTEGER PRIMARY KEY,
    post_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    interaction TEXT CHECK( interaction IN ('UP_VOTE', 'DOWN_VOTE')),
    FOREIGN KEY (user_id) REFERENCES user (id),
    FOREIGN KEY (post_id) REFERENCES post (id)
);


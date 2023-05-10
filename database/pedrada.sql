CREATE TABLE IF NOT EXISTS user(
    id INTEGER PRIMARY KEY,
    public_id VARCHAR(36) NOT NULL,
    pseudonym VARCHAR(20) NOT NULL UNIQUE,
    email VARCHAR(75) NOT NULL UNIQUE,
    user_password VARCHAR(75) NOT NULL,
    registration_date DATE NOT NUll
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
    owner_id INTEGER NOT NULL,
    identified_id INTEGER,
    community_id INTEGER,
    post_description VARCHAR(500) NOT NULL,
    post_time TIMESTAMP NOT NUll,
    post_date DATE NOT NUll,
    FOREIGN KEY (owner_id) REFERENCES user (id),
    FOREIGN KEY (identified_id) REFERENCES user (id),
    FOREIGN KEY (community_id) REFERENCES community (id)
);
CREATE TABLE IF NOT EXISTS post_interaction(
    id INTEGER PRIMARY KEY,
    post_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    interaction TEXT CHECK( interaction IN ('UP_VOTE', 'DOWN_VOTE')),
    FOREIGN KEY (user_id) REFERENCES user (id),
    FOREIGN KEY (post_id) REFERENCES post (id)
);



-- INSERT INTO user(username, e_mail, user_password) 
-- VALUES ("admin", "admin@voleicv.cv", "admin"); 
create table artist(first_name varchar(20), last_name varchar(20), id varchar(10) PRIMARY KEY,
    phone_number varchar(11), age int);
create table exhibition(name varchar(30) PRIMARY KEY, start_date DATE, finish_date DATE);
create table customer(first_name varchar(20), last_name varchar(20), phone_number varchar(11)
    PRIMARY KEY);
create table auction(id int PRIMARY KEY, auc_date DATE, auc_exhibition varchar(30), 
	foreign key(auc_exhibition) references exhibition(name));
create table art_piece(name varchar(20) PRIMARY KEY, description varchar(100), category varchar(20),
    artist_id varchar(10), exhibition varchar(30), price int);
alter table art_piece
    add constraint chk_price check(price >= 1000);
alter table art_piece
    add constraint chk_category check(category = 'photo' OR category = 'sculpture' OR category = 'painting');
alter table art_piece
    add foreign key(artist_id) references artist(id);
alter table art_piece
    add foreign key(exhibition) references exhibition(name);
create table receipt(receipt_no int PRIMARY KEY, customer_no varchar(11), artist_id varchar(10),
    auction_no int, suggested_price int, initial_price int);
alter table receipt
    add foreign key(customer_no) references customer(phone_number);
alter table receipt
    add foreign key(artist_id) references artist(id);
alter table art_piece
    add unique(price);
alter table receipt
    add foreign key(initial_price) references art_piece(price);
alter table receipt
    add constraint check_price check(suggested_price >= 1000);
alter table receipt
    add foreign key(auction_no) references auction(id);
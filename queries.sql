select yelp_restaurant_name, yelp_rating, yelp_review_count, city,
       distance_from_location, yelp_url
from restaurant_data
inner join distances
on restaurant_data.grubhub_restaurant_id = distances.grubhub_restaurant_id
where distances.location_name = 'Fadh'
order by yelp_rating desc, yelp_review_count desc, distance_from_location asc;

order by distance_from_location asc, yelp_rating desc, yelp_review_count desc;
order by yelp_restaurant_name asc;

update locations set max_distance=25 where name='Amma and Abba';

select city, count(*) from restaurant_data group by city order by city;

update restaurant_data set city='San Ramon' where city in ('san ramon');

alter table locations add column max_distance real not null;

SELECT COUNT(1) FROM restaurant_data;


insert into locations values ('Leschi Airbnb', '1311 30th Ave S', 'Seattle', 'WA', 'USA', 47.592030, -122.292964, 5);

insert into locations values ('Fadh', '13929 Marquesas Way', 'Marina del Rey', 'CA', 'USA', 47.592030, -118.4547766, 5);

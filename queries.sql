select yelp_restaurant_name, yelp_rating, yelp_review_count, city,
       distance_from_location, yelp_url
from restaurant_data
inner join distances
on restaurant_data.grubhub_restaurant_id = distances.grubhub_restaurant_id
where distances.location_name = 'Emma'
order by yelp_rating desc, yelp_review_count desc;

update locations set max_distance=25 where name='Amma and Abba';

select city, count(*) from restaurant_data group by city order by city;

update restaurant_data set city='San Ramon' where city in ('san ramon');

alter table locations add column max_distance real not null;

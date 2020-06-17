import turtle
import initial_graphics
import tide_graphics
from tide_time_keeper import tide_time_keeper
import weather_updates
import weather_scraper

#Hide turtle module turtle
turt = turtle.Turtle()
turt.hideturtle()
#Time Stamps

james = 1592399416 #Low Tide morning of 6/13/2020 in Cape Charles Harbor
piank = 1592378296
mobjack = 1592370976

#Location Latitudes and Longitudes
james_lat = '37.5'
james_lon = '-77.4'
piank_lat ='37.5'
piank_lon = '-76.3'
mob_lat = '37.3'
mob_lon = '-76.4'



initial_graphics.win_open()
initial_graphics.tide_scale()
tide_graphics.james_animation(james)
tide_graphics.piank_animation(piank)
tide_graphics.mobjack_animation(mobjack)
weather_updates.slack_update(tide_time_keeper(james), tide_time_keeper(piank), tide_time_keeper(mobjack))
weather_updates.weather_update(weather_scraper.weath(james_lat, james_lon), weather_scraper.weath(piank_lat, piank_lon), weather_scraper.weath(mob_lat, mob_lon))
weather_updates.wind_update(weather_scraper.wind(james_lat, james_lon), weather_scraper.wind_dir(james_lat, james_lon), weather_scraper.wind(piank_lat, piank_lon), weather_scraper.wind_dir(piank_lat, piank_lon), weather_scraper.wind(mob_lat, mob_lon), weather_scraper.wind_dir(mob_lat, mob_lon))



turtle.mainloop()
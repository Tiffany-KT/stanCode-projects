"""
File: Tiffany's drawing
Name: Tiffany
----------------------
I enjoy playing Disney Tsum Tsum game in my free time,
and so I choose to draw the characters from this game.
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    I enjoy playing Disney Tsum Tsum game in my free time,
    and so I choose to draw the characters from this game.
    """
    window = GWindow(width=530, height=700, title="Tiffany's drawing")

    triangle = GPolygon()
    triangle.add_vertex((350, 185))
    triangle.add_vertex((330, 280))
    triangle.add_vertex((500, 265))
    window.add(triangle)
    triangle.color = 'black'
    triangle.filled = True
    triangle.fill_color = 'magenta'

    label = GLabel('SC101')
    label.color = 'white'
    label.font = 'Courier-28-italic'
    window.add(label, 345, 272)

    label_bar = GPolygon()
    label_bar.add_vertex((350, 185))
    label_bar.add_vertex((300, 435))
    label_bar.add_vertex((299, 435))
    window.add(label_bar)
    label_bar.color = 'black'

    # first character: mickey
    mickey = GOval(247, 238, x=70, y=435)
    mickey.color = 'black'
    mickey.filled = True
    mickey.fill_color = 'black'
    window.add(mickey)

    mickey_l_face = GOval(120, 175, x=100, y=460)
    mickey_l_face.color = 'wheat'
    mickey_l_face.filled = True
    mickey_l_face.fill_color = 'wheat'
    window.add(mickey_l_face)

    mickey_r_face = GOval(120, 175, x=170, y=460)
    mickey_r_face.color = 'wheat'
    mickey_r_face.filled = True
    mickey_r_face.fill_color = 'wheat'
    window.add(mickey_r_face)

    mickey_d_face = GOval(217, 133, x=85, y=535)
    mickey_d_face.color = 'wheat'
    mickey_d_face.filled = True
    mickey_d_face.fill_color = 'wheat'
    window.add(mickey_d_face)

    mickey_l_eye = GOval(25, 37, x=145, y=515)
    mickey_l_eye.color = 'black'
    mickey_l_eye.filled = True
    mickey_l_eye.fill_color = 'black'
    window.add(mickey_l_eye)

    mickey_r_eye = GOval(25, 37, x=215, y=515)
    mickey_r_eye.color = 'black'
    mickey_r_eye.filled = True
    mickey_r_eye.fill_color = 'black'
    window.add(mickey_r_eye)

    mickey_nose = GOval(32, 25, x=180, y=565)
    mickey_nose.color = 'black'
    mickey_nose.filled = True
    mickey_nose.fill_color = 'black'
    window.add(mickey_nose)

    mickey_l_blush = GOval(30, 22, x=100, y=580)
    mickey_l_blush.color = 'lightpink'
    mickey_l_blush.filled = True
    mickey_l_blush.fill_color = 'lightpink'
    window.add(mickey_l_blush)

    mickey_r_blush = GOval(30, 22, x=260, y=580)
    mickey_r_blush.color = 'lightpink'
    mickey_r_blush.filled = True
    mickey_r_blush.fill_color = 'lightpink'
    window.add(mickey_r_blush)

    mickey_l_ear = GOval(90, 90, x=45, y=385)
    mickey_l_ear.color = 'black'
    mickey_l_ear.filled = True
    mickey_l_ear.fill_color = 'black'
    window.add(mickey_l_ear)

    mickey_r_ear = GOval(90, 90, x=255, y=385)
    mickey_r_ear.color = 'black'
    mickey_r_ear.filled = True
    mickey_r_ear.fill_color = 'black'
    window.add(mickey_r_ear)

    # second character: alien
    alien = GOval(145, 130, x=65, y=143)
    alien.color = 'greenyellow'
    alien.filled = True
    alien.fill_color = 'greenyellow'
    window.add(alien)

    alien_sign = GOval(28, 23, x=122, y=112)
    alien_sign.color = 'greenyellow'
    alien_sign.filled = True
    alien_sign.fill_color = 'greenyellow'
    window.add(alien_sign)

    alien_bar = GRect(12, 30, x=131, y=120)
    alien_bar.color = 'greenyellow'
    alien_bar.filled = True
    alien_bar.fill_color = 'greenyellow'
    window.add(alien_bar)

    alien_l_ear = GPolygon()
    alien_l_ear.add_vertex((45, 175))
    alien_l_ear.add_vertex((51, 200))
    alien_l_ear.add_vertex((79, 205))
    window.add(alien_l_ear)
    alien_l_ear.color = 'greenyellow'
    alien_l_ear.filled = True
    alien_l_ear.fill_color = 'greenyellow'

    alien_r_ear = GPolygon()
    alien_r_ear.add_vertex((231, 169))
    alien_r_ear.add_vertex((226, 194))
    alien_r_ear.add_vertex((198, 202))
    window.add(alien_r_ear)
    alien_r_ear.color = 'greenyellow'
    alien_r_ear.filled = True
    alien_r_ear.fill_color = 'greenyellow'

    alien_first_eye = GOval(37, 45, x=120, y=180)
    alien_first_eye.color = 'snow'
    alien_first_eye.filled = True
    alien_first_eye.fill_color = 'snow'
    window.add(alien_first_eye)

    alien_first = GOval(23, 23, x=127, y=194)
    alien_first.color = 'black'
    alien_first.filled = True
    alien_first.fill_color = 'black'
    window.add(alien_first)

    alien_second_eye = GOval(37, 45, x=85, y=190)
    alien_second_eye.color = 'snow'
    alien_second_eye.filled = True
    alien_second_eye.fill_color = 'snow'
    window.add(alien_second_eye)

    alien_second = GOval(22, 22, x=95, y=206)
    alien_second.color = 'black'
    alien_second.filled = True
    alien_second.fill_color = 'black'
    window.add(alien_second)

    alien_third_eye = GOval(37, 45, x=156, y=185)
    alien_third_eye.color = 'snow'
    alien_third_eye.filled = True
    alien_third_eye.fill_color = 'snow'
    window.add(alien_third_eye)

    alien_third = GOval(22, 22, x=162, y=201)
    alien_third.color = 'black'
    alien_third.filled = True
    alien_third.fill_color = 'black'
    window.add(alien_third)

    # third character: pooh
    pooh_headband = GOval(165, 155, x=111, y=262)
    pooh_headband.color = 'brown'
    pooh_headband.filled = True
    pooh_headband.fill_color = 'brown'
    window.add(pooh_headband)

    pooh_l_band = GRect(6, 30, x=160, y=250)
    pooh_l_band.color = 'brown'
    pooh_l_band.filled = True
    pooh_l_band.fill_color = 'brown'
    window.add(pooh_l_band)

    pooh_l_headband = GOval(18, 18, x=153, y=237)
    pooh_l_headband.color = 'tomato'
    pooh_l_headband.filled = True
    pooh_l_headband.fill_color = 'tomato'
    window.add(pooh_l_headband)

    pooh_r_band = GRect(6, 30, x=220, y=250)
    pooh_r_band.color = 'brown'
    pooh_r_band.filled = True
    pooh_r_band.fill_color = 'brown'
    window.add(pooh_r_band)

    pooh_r_headband = GOval(18, 18, x=213, y=237)
    pooh_r_headband.color = 'tomato'
    pooh_r_headband.filled = True
    pooh_r_headband.fill_color = 'tomato'
    window.add(pooh_r_headband)

    pooh = GOval(180, 170, x=105, y=270)
    pooh.color = 'orange'
    pooh.filled = True
    pooh.fill_color = 'orange'
    window.add(pooh)

    pooh_l_eyebrow = GOval(30, 30, x=140, y=310)
    pooh_l_eyebrow.color = 'brown'
    pooh_l_eyebrow.filled = True
    pooh_l_eyebrow.fill_color = 'brown'
    window.add(pooh_l_eyebrow)

    pooh_l_eyebrow_cut = GOval(33, 35, x=142, y=315)
    pooh_l_eyebrow_cut.color = 'orange'
    pooh_l_eyebrow_cut.filled = True
    pooh_l_eyebrow_cut.fill_color = 'orange'
    window.add(pooh_l_eyebrow_cut)

    pooh_r_eyebrow = GOval(30, 30, x=218, y=310)
    pooh_r_eyebrow.color = 'brown'
    pooh_r_eyebrow.filled = True
    pooh_r_eyebrow.fill_color = 'brown'
    window.add(pooh_r_eyebrow)

    pooh_r_eyebrow_cut = GOval(33, 35, x=215, y=315)
    pooh_r_eyebrow_cut.color = 'orange'
    pooh_r_eyebrow_cut.filled = True
    pooh_r_eyebrow_cut.fill_color = 'orange'
    window.add(pooh_r_eyebrow_cut)

    pooh_l_eye = GOval(19, 22, x=160, y=340)
    pooh_l_eye.color = 'brown'
    pooh_l_eye.filled = True
    pooh_l_eye.fill_color = 'brown'
    window.add(pooh_l_eye)

    pooh_r_eye = GOval(19, 22, x=210, y=340)
    pooh_r_eye.color = 'brown'
    pooh_r_eye.filled = True
    pooh_r_eye.fill_color = 'brown'
    window.add(pooh_r_eye)

    pooh_nose = GPolygon()
    pooh_nose.add_vertex((196, 394))
    pooh_nose.add_vertex((181, 382))
    pooh_nose.add_vertex((211, 382))
    window.add(pooh_nose)
    pooh_nose.color = 'brown'
    pooh_nose.filled = True
    pooh_nose.fill_color = 'brown'

    pooh_nose_plus = GOval(28, 15, x=182, y=374)
    pooh_nose_plus.color = 'brown'
    pooh_nose_plus.filled = True
    pooh_nose_plus.fill_color = 'brown'
    window.add(pooh_nose_plus)

    pooh_l_ear = GOval(35, 38, x=99, y=278)
    pooh_l_ear.color = 'orange'
    pooh_l_ear.filled = True
    pooh_l_ear.fill_color = 'orange'
    window.add(pooh_l_ear)

    pooh_r_ear = GOval(35, 38, x=255, y=278)
    pooh_r_ear.color = 'orange'
    pooh_r_ear.filled = True
    pooh_r_ear.fill_color = 'orange'
    window.add(pooh_r_ear)

    # forth character: olaf
    olaf_hair = GRect(3, 13, x=233, y=61)
    olaf_hair.color = 'black'
    olaf_hair.filled = True
    olaf_hair.fill_color = 'black'
    window.add(olaf_hair)

    olaf_l_hair = GPolygon()
    olaf_l_hair.add_vertex((238, 81))
    olaf_l_hair.add_vertex((218, 68))
    olaf_l_hair.add_vertex((218, 72))
    window.add(olaf_l_hair)
    olaf_l_hair.color = 'black'
    olaf_l_hair.filled = True
    olaf_l_hair.fill_color = 'black'

    olaf_r_hair = GPolygon()
    olaf_r_hair.add_vertex((238, 79))
    olaf_r_hair.add_vertex((258, 65))
    olaf_r_hair.add_vertex((258, 70))
    window.add(olaf_r_hair)
    olaf_r_hair.color = 'black'
    olaf_r_hair.filled = True
    olaf_r_hair.fill_color = 'black'

    olaf = GOval(120, 110, x=175, y=75)
    olaf.color = 'skyblue'
    olaf.filled = True
    olaf.fill_color = 'snow'
    window.add(olaf)

    olaf_teeth_one = GRect(20, 8, x=217, y=159)
    olaf_teeth_one.color = 'skyblue'
    window.add(olaf_teeth_one)
    olaf_teeth_two = GRect(20, 8, x=237, y=159)
    olaf_teeth_two.color = 'skyblue'
    window.add(olaf_teeth_two)

    olaf_mouth = GOval(60, 10, x=207, y=152)
    olaf_mouth.color = 'skyblue'
    olaf_mouth.filled = True
    olaf_mouth.fill_color = 'snow'
    window.add(olaf_mouth)
    olaf_mouth_cut = GOval(60, 10, x=207, y=150)
    olaf_mouth_cut.color = 'snow'
    olaf_mouth_cut.filled = True
    olaf_mouth_cut.fill_color = 'snow'
    window.add(olaf_mouth_cut)

    olaf_l_eyebrow = GOval(25, 25, x=200, y=100)
    olaf_l_eyebrow.color = 'brown'
    olaf_l_eyebrow.filled = True
    olaf_l_eyebrow.fill_color = 'brown'
    window.add(olaf_l_eyebrow)

    olaf_l_eyebrow_cut = GOval(29, 32, x=200, y=102)
    olaf_l_eyebrow_cut.color = 'snow'
    olaf_l_eyebrow_cut.filled = True
    olaf_l_eyebrow_cut.fill_color = 'snow'
    window.add(olaf_l_eyebrow_cut)

    olaf_r_eyebrow = GOval(25, 25, x=250, y=100)
    olaf_r_eyebrow.color = 'brown'
    olaf_r_eyebrow.filled = True
    olaf_r_eyebrow.fill_color = 'brown'
    window.add(olaf_r_eyebrow)

    olaf_r_eyebrow_cut = GOval(29, 32, x=247, y=102)
    olaf_r_eyebrow_cut.color = 'snow'
    olaf_r_eyebrow_cut.filled = True
    olaf_r_eyebrow_cut.fill_color = 'snow'
    window.add(olaf_r_eyebrow_cut)

    olaf_l_eye = GOval(18, 18, x=210, y=115)
    olaf_l_eye.color = 'black'
    olaf_l_eye.filled = True
    olaf_l_eye.fill_color = 'black'
    window.add(olaf_l_eye)

    olaf_r_eye = GOval(18, 18, x=246, y=115)
    olaf_r_eye.color = 'black'
    olaf_r_eye.filled = True
    olaf_r_eye.fill_color = 'black'
    window.add(olaf_r_eye)

    olaf_nose = GOval(26, 27, x=224, y=127)
    olaf_nose.color = 'coral'
    olaf_nose.filled = True
    olaf_nose.fill_color = 'coral'
    window.add(olaf_nose)

    # fifth character: car
    car_l_mirror = GRect(12, 23, x=232, y=181)
    car_l_mirror.color = 'darkred'
    car_l_mirror.filled = True
    car_l_mirror.fill_color = 'red'
    window.add(car_l_mirror)

    car_r_mirror = GRect(12, 23, x=320, y=181)
    car_r_mirror.color = 'darkred'
    car_r_mirror.filled = True
    car_r_mirror.fill_color = 'red'
    window.add(car_r_mirror)

    car = GOval(110, 102, x=227, y=177)
    car.color = 'darkred'
    car.filled = True
    car.fill_color = 'red'
    window.add(car)

    car_l_glass = GRect(37, 35, x=247, y=200)
    car_l_glass.color = 'white'
    car_l_glass.filled = True
    car_l_glass.fill_color = 'white'
    window.add(car_l_glass)
    car_r_glass = GRect(37, 35, x=277, y=203)
    car_r_glass.color = 'white'
    car_r_glass.filled = True
    car_r_glass.fill_color = 'white'
    window.add(car_r_glass)

    car_l_eye = GOval(13, 13, x=265, y=217)
    car_l_eye.color = 'black'
    car_l_eye.filled = True
    car_l_eye.fill_color = 'black'
    window.add(car_l_eye)
    car_r_eye = GOval(13, 13, x=285, y=217)
    car_r_eye.color = 'black'
    car_r_eye.filled = True
    car_r_eye.fill_color = 'black'
    window.add(car_r_eye)

    car_one = GOval(37, 37, x=261, y=232)
    car_one.color = 'red'
    car_one.filled = True
    car_one.fill_color = 'red'
    window.add(car_one)
    car_two = GOval(35, 35, x=238, y=233)
    car_two.color = 'red'
    car_two.filled = True
    car_two.fill_color = 'red'
    window.add(car_two)
    car_three = GOval(35, 35, x=284, y=233)
    car_three.color = 'red'
    car_three.filled = True
    car_three.fill_color = 'red'
    window.add(car_three)

    car_l_light = GRect(15, 7, x=240, y=243)
    car_l_light.color = 'yellow'
    car_l_light.filled = True
    car_l_light.fill_color = 'yellow'
    window.add(car_l_light)
    car_l_light_plus = GRect(12, 7, x=248, y=243)
    car_l_light_plus.color = 'grey'
    car_l_light_plus.filled = True
    car_l_light_plus.fill_color = 'grey'
    window.add(car_l_light_plus)

    car_r_light = GRect(15, 7, x=310, y=243)
    car_r_light.color = 'yellow'
    car_r_light.filled = True
    car_r_light.fill_color = 'yellow'
    window.add(car_r_light)
    car_r_light_plus = GRect(12, 7, x=302, y=243)
    car_r_light_plus.color = 'grey'
    car_r_light_plus.filled = True
    car_r_light_plus.fill_color = 'grey'
    window.add(car_r_light_plus)


if __name__ == '__main__':
    main()

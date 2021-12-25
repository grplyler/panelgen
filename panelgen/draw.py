
# a rectangle that wraps round on x and y
def wrap_rect(c, x, y, w, h, rgb):

    # setup pen
    c.set_source_rgb(*rgb)

    # draw first rect
    c.rectangle(x, y, w, h)

    # calulate right side overlap
    x_over = 1.0 - (x + w)
    y_over = 1.0 - (y + h)
    x_wrap = abs(x_over)
    y_wrap = abs(y_over)

    # If over are negative, we need to wrap the image
    if x_over < 0.0:
        # wrap x wrap
        c.rectangle(0.0, y, x_wrap, h)

    if y_over < 0.0:
        y_wrap = abs(y_over)
        c.rectangle(x, 0.0, w, y_wrap)

    # if x and y are over:
    if x_over < 0.0 and y_over < 0.0:
        print('xy wrap')
        c.rectangle(0.0, 0.0, x_wrap, y_wrap)

    c.fill()
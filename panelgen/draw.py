from PIL import Image, ImageChops

def wrap_texture(base, tex, x, y, tcnf):
    x = round(base.width * x)
    y = round(base.height * y)
    elev = round(255 * tcnf.rand['texture.elevation'])

    # Set height of texture
    mult = Image.new('RGBA', tex.size, (elev, elev, elev))
    tex = ImageChops.multiply(tex, mult)

    # find x overlap
    x_over = base.width - (x + tex.width)
    y_over = base.height - (y + tex.height)

    if x_over < 0:
        left = tex.width - abs(x_over)
        top = 0
        right = tex.width
        bottom = tex.height
        crop = tex.crop((left, top, right, bottom))
        base.paste(crop, (0, y), crop)

    if y_over < 0:
        left = 0
        top = tex.height - abs(y_over)
        right = tex.width
        bottom = tex.height
        crop = tex.crop((left, top, right, bottom))
        base.paste(crop, (x, 0), crop)

    if y_over < 0 and x_over < 0:
        left = tex.width - abs(x_over)
        top = tex.height - abs(y_over)
        right = tex.width
        bottom = tex.height
        crop = tex.crop((left, top, right, bottom))
        base.paste(crop, (0, 0), crop)

    base.paste(tex, (x, y), tex)

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
        c.rectangle(0.0, 0.0, x_wrap, y_wrap)

    c.fill()
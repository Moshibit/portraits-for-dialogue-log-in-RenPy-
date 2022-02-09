# The MIT License (MIT)
#
# Copyright 2022 Erik Juárez-Guerrero <https://github.com/Moshibit>
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

init python:
    def image_history_callback(entry):
        tag = entry.image_tag

        # Constants
        IMAGE_DIRECTORY = "gui/history/"
        IMAGE_PREFIX = "history"
        IMAGE_EXTENSION = ".png"

        # None when the character is not assigned an image tag.
        if tag is None:
            entry.image = None
            return

        # create the image property on the entry object.
        if tag == "generic":
            entry.image = "{}{} generic{}".format(IMAGE_DIRECTORY, IMAGE_PREFIX,IMAGE_EXTENSION)
            return
        if tag == "generic_girl":
            entry.image = "{}{} generic girl{}".format(IMAGE_DIRECTORY, IMAGE_PREFIX,IMAGE_EXTENSION)
            return
        if tag == "generic_boy":
            entry.image = "{}{} generic boy{}".format(IMAGE_DIRECTORY, IMAGE_PREFIX,IMAGE_EXTENSION)
            return

        # get the attributes of the current image
        attributes = renpy.get_attributes(tag) # attribute tuple

        # handling None atrributes
        if attributes is not None:
            attributes = " ".join(attributes) # the tuple is now a string
        else:
            attributes = ""

        # get the image to show, choose only one:
        # * uncomment next line if you want the same image every time
        # image_string = "{}{} {}{}".format(IMAGE_DIRECTORY, IMAGE_PREFIX, tag, IMAGE_EXTENSION)

        # * or uncomment next line if you want the image to match the current attributes
        image_string = "{}{} {} {}{}".format(IMAGE_DIRECTORY, IMAGE_PREFIX, tag, attributes, IMAGE_EXTENSION)

        # handling missing images
        if renpy.exists(image_string) == False:
            if config.developer:
                image_string = "{}{} missing{}".format(IMAGE_DIRECTORY, IMAGE_PREFIX,IMAGE_EXTENSION)
            else:
                image_string = None

        # create the image property on the entry object
        entry.image = image_string
        return

    # add the callback function to the configuration variable
    config.history_callbacks.append(image_history_callback)

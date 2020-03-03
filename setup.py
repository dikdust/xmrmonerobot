# xmrmonerobot - check cryptocurrencies prices on telegram
# Copyright (C) 2020  dikdust <dikdust@gmail.com> <github.com/dikdust>
#
# xmrmonerobot is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# xmrmonerobot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with xmrmonerobot.  If not, see <http://www.gnu.org/licenses/>.

import json
import setuptools



setuptools.setup(

    name="cryptotrackerbot",
    version="1",

    license="AGPL-3.0",

    author="dikdust",
    author_email="dikdust@gmail.com",

    install_requires=[
        "python-telegram-bot",
        "requests",
        "mplfinance",
        "image"
    ],

    packages=[
        "cryptotrackerbot",
    ],

    entry_points={
        "console_scripts": [
            "cryptotrackerbot = cryptotrackerbot.__main__:main",
        ],
    },

    include_package_data=True,
    zip_safe=False,

    classifiers=[
        "Not on PyPI"
    ],

)

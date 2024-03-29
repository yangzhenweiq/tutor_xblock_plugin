from setuptools import setup


setup(
    name="tutor-xpoll",
    version="0.0.1",
    license="AGPLv3",
    author="yzw",
    author_email="327874145@qq.com",
    description="A Tutor plugin for xblock in cms",
    packages=["tutorxpoll"],
    include_package_data=True,
    python_requires=">=3.5",
    entry_points={"tutor.plugin.v0": ["xpoll = tutorxpoll.plugin"]},
)

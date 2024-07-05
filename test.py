from flask import Flask, render_template, session, request, redirect, url_for
import random

num = random.randint(0, 6)
print(num)

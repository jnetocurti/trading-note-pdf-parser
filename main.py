#!/usr/bin/env python3

import click
from src.domain.service.note_service import NoteService
from src.domain.utils.presenters import to_json as json, to_csv as csv


@click.group()
def app():
    pass


@app.command()
@click.argument("file_path")
def to_json(file_path: str):
    if note := NoteService.parse(file_path):
        print(json(note))


@app.command()
@click.argument("file_path")
def to_csv(file_path: str):
    if note := NoteService.parse(file_path):
        print(csv(note))


if __name__ == "__main__":
    app()

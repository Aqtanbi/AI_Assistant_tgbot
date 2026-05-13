class NoteIterator:
    """Custom iterator for showing saved notes one by one."""

    def __init__(self, notes: list[dict]) -> None:
        self.notes = notes
        self.index = 0

    def __iter__(self) -> "NoteIterator":
        return self

    def __next__(self) -> dict:
        if self.index >= len(self.notes):
            raise StopIteration

        note = self.notes[self.index]
        self.index += 1
        return note

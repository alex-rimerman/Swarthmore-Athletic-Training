function deleteNote(noteId, role) {
    fetch("/delete-note", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
        if (role == "trainer") {
            window.location.href = "/trainerHome";
        } else {
            window.location.href = "/";
        }
    });
}
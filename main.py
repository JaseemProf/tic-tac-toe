from fasthtml.common import *
from monsterui.all import *

hdrs = (Theme.blue.headers(), Link(rel="stylesheet", href="/public/style.css"))
app, rt = fast_app(hdrs=hdrs, live=True)


@app.get("/")
def index():
    def render_block(_):
        return Div(
            cls="cell bg-gray-200 flex justify-center items-center text-5xl font-bold text-gray-700 cursor-pointer rounded-lg transition-colors duration-200 hover:bg-gray-300"
        )

    game_area = Div(
        H1("Tic Tac Toe", cls="text-4xl font-extrabold text-gray-900 mb-6 sm:text-3xl"),
        Div(
            "Player X's Turn",
            id="gameStatus",
            cls="status text-2xl font-semibold mb-4 text-gray-800 sm:text-xl",
        ),
        Div(
            *map(render_block, range(9)),
            cls="board grid grid-cols-3 grid-rows-3 gap-2 w-full mx-auto my-6",
        ),
        Button("Reset Game", id="resetButton"),
        cls="game-container bg-white p-8 rounded-2xl shadow-xl max-w-sm w-full text-center sm:p-6",
    )
    return Div(
        game_area,
        cls="font-inter bg-gray-100 flex justify-center items-center min-h-screen m-0 p-4 box-border",
    )


serve()

defmodule PassCapchaWeb.PageController do
  use PassCapchaWeb, :controller

  def pass_capcha(conn, params) do
    {ok, binary} =  Base.decode64(params["capcha"])
    File.write!("input.jpg", binary)
    {text, _} = System.cmd("python3", ["pass_capcha.py"])
    j = text
    |> String.trim()
    |> String.replace(" ", "")
    json conn, %{capcha: j}
  end
end

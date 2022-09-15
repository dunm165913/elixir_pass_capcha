defmodule PassCapcha.Repo do
  use Ecto.Repo,
    otp_app: :pass_capcha,
    adapter: Ecto.Adapters.Postgres
end

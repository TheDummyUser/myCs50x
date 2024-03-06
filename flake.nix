{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    systems.url = "github:nix-systems/default";
    devenv.url = "github:cachix/devenv";
  };

  outputs = { nixpkgs, devenv, systems, ... }@inputs:
    let forEachSystem = nixpkgs.lib.genAttrs (import systems);
    in {
      devShells = forEachSystem (system:
        let pkgs = nixpkgs.legacyPackages.${system};
        in {
          default = devenv.lib.mkShell {
            inherit inputs pkgs;
            modules = [{
              # https://devenv.sh/reference/options/
              packages = with pkgs; [
                nodejs
                nodePackages.pyright
                nodePackages_latest.expo-cli
                libcs50
                cmake
                android-tools
                #python-language-server
              ];

              dotenv.disableHint = true;
              languages.c.enable = true;
              languages.javascript.enable = true;
              languages.python = {
                enable = true;
                package = pkgs.python3.withPackages (ps:
                  with ps; [
                    black
                    python-lsp-server
                    cryptography
                    flask
                    tkinter
                  ]);
                venv.enable = true;
              };

            }];
          };
        });
    };
}

from typing import Optional, Union

class Passphrase:
  _s: Optional[str]
  _is_destroyed: bool = False

  def __init__(self, passphrase: Optional[Union['Passphrase', str]], none_value: Optional[str]=None):
    if isinstance(passphrase, Passphrase):
      if passphrase._is_destroyed:
        raise RuntimeError(f"{passphrase} has been destroyed")
      self._s = passphrase._s
    else:
      if passphrase == none_value:
        passphrase = None
      self._s = passphrase

  def __str__(self) -> str:
    # Do not reveal potentially secret data by accident in logs, etc
    return f"<Passphrase @{self.id}{' [DESTROYED]' if self._is_destroyed else ''}>"

  def get_cleartext(self) -> str:
    if self._is_destroyed:
      raise RuntimeError(f"{self} has been destroyed")
    return self._s

  def clone(self) -> 'Passphrase':
    return Passphrase(self)

  def destroy(self):
    self._s = None
    self._is_destroyed = True

  def __del__(self):
    self.destroy()


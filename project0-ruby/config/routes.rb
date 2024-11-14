Rails.application.routes.draw do
        get '/pets', to: 'pets#index'
        post '/pets', to: 'pets#create'
        get '/pets/:id', to: 'pets#show'
        patch '/pets/:id', to: 'pets#update'
        delete '/pets/:id', to: 'pets#destroy'

        get '/owners', to: 'owners#index'
        post '/owners', to: 'owners#create'
        get '/owners/:id', to: 'owners#show'
        get '/owners/:id/pets', to: 'owners#pets'
        patch '/owners/:id', to: 'owners#update'
        delete '/owners/:id', to: 'owners#destroy'

  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end

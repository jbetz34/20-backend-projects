require 'test_helper'

class OwnersControllerTest < ActionDispatch::IntegrationTest
  test "should get index" do
    get owners_index_url
    assert_response :success
  end

  test "should get create" do
    get owners_create_url
    assert_response :success
  end

  test "should get show" do
    get owners_show_url
    assert_response :success
  end

  test "should get update" do
    get owners_update_url
    assert_response :success
  end

  test "should get destroy" do
    get owners_destroy_url
    assert_response :success
  end

end
